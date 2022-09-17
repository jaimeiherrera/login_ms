from sqlalchemy.orm import Session

from ..utils import encoder
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email, password=encoder(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_tokens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Token).offset(skip).limit(limit).all()


def create_user_token(db: Session, token: schemas.TokenCreate, user_id: int):
    user = get_user(db=db, user_id=user_id)
    db_token = models.Token(**token.dict(), owner=user)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token
