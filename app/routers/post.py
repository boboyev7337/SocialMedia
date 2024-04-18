from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.database import get_db
from app.models import Post
from app.schemes import PostCreate, PostOutPut, UserOutPut
from app.services.oauth2 import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=PostOutPut)
def post_create(data: PostCreate, db=Depends(get_db), user: UserOutPut = Depends(get_current_user)):
    print(data, '----', user)
    new_post = Post(**data.dict(), owner_i=user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# @router.get('/get', status_code=status.HTTP_200_OK)
# def post_get():
#     pass