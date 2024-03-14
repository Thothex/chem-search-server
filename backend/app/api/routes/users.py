from typing import List

from app.crud.crud_user import (
    create_user,
    get_user,
    get_user_by_email,
    get_users,
    update_user_password,
)
from app.db.postgresql.session import SessionLocal
from app.schemas.user import User, UserCreate, UserUpdatePassword
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/users/", response_model=List[User])
def read_users(
    skip: int = Query(default=0, description="Number of users to skip"),
    limit: int = Query(default=10, description="Max number of users to return"),
    db: Session = Depends(get_db),
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}/change-password", response_model=User)
def change_user_password_route(
    user_id: int, user_pass: UserUpdatePassword, db: Session = Depends(get_db)
):
    updated_user = update_user_password(db, user_id, user_pass)
    if not updated_user:
        raise HTTPException(status_code=400, detail="Password update failed")
    return updated_user
