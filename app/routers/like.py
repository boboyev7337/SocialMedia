from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.schemes import LikeSchema
from app.services.oauth2 import get_current_user
from app.models import Like, Post

router = APIRouter(prefix="/like", tags=["like"])


@router.post('/', status_code=status.HTTP_201_CREATED)
def like_to_post(data: LikeSchema, db: Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == data.post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    like = db.query(Like).filter(Like.post_id == post.id, Like.owner_id == current_user.id)
    if like.count() == 0:
        new_like = Like(post_id=post.id, owner_id=current_user.id)
        db.add(new_like)
        db.commit()
        db.refresh(new_like)
        return {"message": "Post has been liked"}
    else:
        like.delete()
        db.commit()
        return {"message": "Post has been unliked"}