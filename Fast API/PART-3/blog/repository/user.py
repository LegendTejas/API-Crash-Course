from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from .. hashing import Hash #importing Hash class from hashing.py file


def create(request: schemas.ShowUser, db:Session):
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

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with this id {id} is not available")
    
    return user