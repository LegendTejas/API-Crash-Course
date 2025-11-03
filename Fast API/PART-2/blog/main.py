from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash #importing Hash class from hashing.py file

app = FastAPI()

# Create database tables (if they don't already exist)
models.Base.metadata.create_all(engine)


# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a blog (POST)
@app.post('/blog', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)):
    # Automatically assign user_id (e.g., 1)
    default_user_id = 1

    # Check if user exists
    user = db.query(models.User).filter(models.User.id == default_user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {default_user_id} not found. Please create a user first."
        )

    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=default_user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Delete a blog by ID (DELETE) - return JSON message with 200 OK
@app.delete('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blogs'])
def destroy(id: int, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}


# Update a blog by ID (PUT)
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id: int, request: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.update(request.dict())
    db.commit()
    return {"message": "Updated successfully"}


# Get all blogs (GET)
@app.get('/blog', response_model=list[schemas.ShowBlog], tags=['blogs'])
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# Get a single blog by ID (GET)
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog


# Create user (POST)
@app.post('/user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED, tags=['users'])
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    # optional: simple duplicate email check
    existing = db.query(models.User).filter(models.User.email == request.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists"
        )
    new_user = models.User(
        name=request.name,
        email=request.email,
        password= Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with this id {id} is not available")
    
    return user