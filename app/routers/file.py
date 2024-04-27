import tempfile

from fastapi import APIRouter, Depends, UploadFile, File

MINIO_ACCESS_KEY = "CE83an5vfa3tyjmamlmf"
MINIO_SECRET_KEY = "dX472ntGOi5vht2BKduhXfbzA4KhF7G6bzjhko8v"

router = APIRouter(prefix="/files", tags=["files"])

from minio import Minio

client = Minio("127.0.0.1:9000",
               access_key=MINIO_ACCESS_KEY,
               secret_key=MINIO_SECRET_KEY,
               secure=False
               )


@router.post("/")
def file_upload(file: UploadFile = File(...)):
    handler, path = tempfile.mkstemp(suffix=f"{file.filename.split('.')[-1]}")
    with open(path, "wb") as f:
        f.write(file.file.read())
    client.fput_object(
        'images', file.filename, path
    )

    return {'file': file.filename}