from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    password: str


class UserOutput(BaseModel):
    created: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr