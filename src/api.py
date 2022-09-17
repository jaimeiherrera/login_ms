from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .db import crud, models, schemas
from .db.database import SessionLocal, engine
from .jwt_utils import decode_jwt, encode_jwt

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="login_ms")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/test")
def test():
    encoded = encode_jwt()
    decoded = decode_jwt(encoded)
    return None


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/tokens/", response_model=schemas.Token)
def create_item_for_user(
    user_id: int, token: schemas.TokenCreate, db: Session = Depends(get_db)
):
    return crud.create_user_token(db=db, token=token, user_id=user_id)


@app.get("/tokens/", response_model=list[schemas.Token])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_tokens(db, skip=skip, limit=limit)
    return items



@app.get("/")
def root():
    return {"message": "Welcome to login_ms!"}
