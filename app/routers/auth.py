from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.models import User
from app.schemes import Token
from app.services.oauth2 import create_access_token
from app.services.utils import verify

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login', status_code=200, response_model=Token)
def login(user: OAuth2PasswordRequestForm=Depends(), db=Depends(get_db())):
    query = db.query(User).filter(User.email == user.email).first()

    if not query:
        raise HTTPException(status_code=409, detail="Invalid User email")

    if not verify(user.password, query.password):
        raise HTTPException(status_code=409, detail="Invalid User password")

    access_token = create_access_token(data={'user.id': query.id})

    return {

    }