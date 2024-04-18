from fastapi import FastAPI

from app.routers.user import router as user_router
from app.routers.auth import router as auth_router
from app.routers.post import router as post_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(post_router)