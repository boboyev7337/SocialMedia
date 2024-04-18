from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    # class Config:
    #     orm_mode = True


class UserOutPut(BaseModel):
    created: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int


class CommentCreate(BaseModel):
    post_id: int
    content: str


class CommentOutPut(CommentCreate):
    id: int
    content: str
    created: datetime


class PostCreate(BaseModel):
    title: str
    content: str


class PostOutPut(PostCreate):
    id: int
    created: datetime
    owner: UserOutPut


class PostOutPutAll(PostCreate):
    id: int
    created: datetime
    comments: list[CommentOutPut]


class LikeSchemas(BaseModel):
    post_id: int