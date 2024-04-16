from datetime import datetime, timezone, timedelta

from jose import jwt

SECRET_KEY = "test"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPORE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    exipre = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPORE_MINUTES)
    to_encode.update({"exp": exipre})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt