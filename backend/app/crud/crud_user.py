from app.models.user import User
from app.schemas.user import UserCreate, UserUpdatePassword
from passlib.context import CryptContext
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email, username=user.username, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_password(
    db: Session, user_id: int, user_pass: UserUpdatePassword
) -> User:
    user = get_user(db, user_id)
    if user and pwd_context.verify(user_pass.old_password, user.hashed_password):
        user.hashed_password = pwd_context.hash(user_pass.new_password)
        db.commit()
        return user
    return None


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
