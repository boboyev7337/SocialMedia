from fastapi import FastAPI

from app.routers.user import router as user_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}

app.include_router(user_router)