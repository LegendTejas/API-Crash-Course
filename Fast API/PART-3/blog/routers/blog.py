from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


# ---------- Get all blogs ----------
@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(
    db: Session = Depends(get_db),
    current_user: schemas.UserBase = Depends(oauth2.get_current_user)
):
    return blog.get_all(db)


# ---------- Create a new blog ----------
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create_blog(
    request: schemas.BlogCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserBase = Depends(oauth2.get_current_user)
):
    return blog.create(request, db)


# ---------- Delete a blog ----------
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserBase = Depends(oauth2.get_current_user)
):
    return blog.destroy(id, db)


# ---------- Update a blog ----------
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog)
def update_blog(
    id: int,
    request: schemas.BlogUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.UserBase = Depends(oauth2.get_current_user)
):
    return blog.update(id, request, db)


# ---------- Get a specific blog ----------
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserBase = Depends(oauth2.get_current_user)
):
    return blog.show(id, db)