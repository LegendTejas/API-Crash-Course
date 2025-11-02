from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

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


# -----------------------------
# Create a new blog (POST)
# -----------------------------
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    # Create a new Blog model instance
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)       # Add to session
    db.commit()            # Save changes
    db.refresh(new_blog)   # Refresh to get new ID
    return new_blog


# -----------------------------
# Delete a blog by ID (DELETE)
# -----------------------------
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    # Query the blog by ID
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    # If blog doesn't exist, raise a 404 error
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    # Delete the blog if found
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}


# -----------------------------
# Update a blog by ID (PUT)
# -----------------------------
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    # If the blog doesn't exist, raise a 404
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    # Update the blog with new data (convert Pydantic model to dict)
    blog.update(request.dict())
    db.commit()
    return {"message": "Updated successfully"}


# -----------------------------
# Get all blogs (GET)
# -----------------------------
@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# -----------------------------
# Get a single blog by ID (GET)
# -----------------------------
@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(get_db)):
    # Fetch a blog by its ID
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # If not found, raise a 404
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog