from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.BlogCreate, db: Session):
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

def delete(id: int, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}

def update(id: int, request: schemas.BlogUpdate , db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.update(request.dict())
    db.commit()
    return {"message": "Updated successfully"}

def show(id : int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog