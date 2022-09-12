from pydantic import BaseModel


class TokenBase(BaseModel):
    token: str


class ItemCreate(TokenBase):
    pass


class Token(TokenBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Token] = []

    class Config:
        orm_mode = True
