from datetime import datetime, timezone, timedelta

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.database import get_db
from app.models import User
from app.schemes import TokenData

SECRET_KEY = "test"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPLORE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def create_access_token(data: dict):
    to_encode = data.copy()

    exipre = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPLORE_MINUTES)
    to_encode.update({"exp": exipre})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=400, detail="Token expired")

        # token_data = TokenData(user_id=payload.get('user_id'))
        # print(token_data)
    except JWTError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_id


def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    user_id = verify_access_token(token)
    user = db.query(User).filter(User.id == user_id.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user