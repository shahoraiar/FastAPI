from fastapi import FastAPI, Form, File, UploadFile
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    username : str
    password : str

@app.post('/login/') 
async def login(data: Annotated[FormData, Form()]):
    print('type : ', type(data))
    print('form : ', data)
    return data

@app.post('/files/')
async def create_file(data: Annotated[bytes, File(description="A file read as bytes")] = None):
    return {"file_size": len(data)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    return {"filename": file.filename}




