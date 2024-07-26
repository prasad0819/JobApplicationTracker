from fastapi import APIRouter
from typing import List
from app import crud, database, schemas
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.CreateUser, db: Session = Depends(database.get_db)):
    # db_user = crud.get_user_by_email(email=user.email, db=db)
    # if db_user:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return crud.create_user(user=user, db=db)


@router.get("/", response_model=List[schemas.ShowUser])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.ShowUser)
def read_user_by_id(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.get("/{email}", response_model=schemas.ShowUser)
def read_user_by_email(email: str, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.delete("/{id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    user_delete = delete_user(db, user_id=user_id)
    return user_delete
