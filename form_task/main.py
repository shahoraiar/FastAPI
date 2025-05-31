# https://docs.google.com/document/d/1dShtXKE1Q5qMJwlLkQBr_sgYZ2utbhAIlgWCtsDnmo8/edit?tab=t.0

from fastapi import FastAPI, File, Form, UploadFile
from typing import Annotated
from pydantic import BaseModel
import random

app = FastAPI()

#🧪 টাস্ক ১: একক ফাইল আপলোড
    #একটি API তৈরি করুন যেখানে একজন ইউজার একটি ফাইল আপলোড করতে পারবে।
    #ফাইলের নাম, ধরন এবং সাইজ রেসপন্স হিসেবে পাঠান।

@app.post('/single/file/upload/')
def single_file_upload(file1: Annotated[UploadFile, File(description='File contains filename')],
                       file2: Annotated[bytes, File(description='File Contains Bytes')]= None):
    return {
        'status': 'success',
        'file 2 name': file1.filename,
        'file 2 type': file1.content_type,
        'file 1 size': len(file2) if file2 else 0
    }

#🧪 টাস্ক ২: একাধিক ফাইল আপলোড
    #এমন একটি API বানান যেখানে একাধিক ফাইল আপলোড করা যাবে।
    #প্রতিটি ফাইলের নাম ও টাইপ দেখান।

@app.post('/multifile/upload/')
async def multi_file_upload(files: list[UploadFile]= File(description='Upload Your File')):
    result = []
    for file in files:
        result.append({
            "filename": file.filename,
            "content_type": file.content_type
        })
    return {
        'status': 'success',
        'files': result
    }

# 🧪 টাস্ক ৩: ফর্ম ডেটা ও ফাইল একসাথে আপলোড
    #এমন একটি API তৈরি করুন যেখানে ইউজার একটি ফর্ম পূরণ করবে (যেমন: নাম ও বয়স) এবং একটি ফাইল আপলোড করবে।
    #ফর্মের তথ্য ও ফাইলের নাম রেসপন্স হিসেবে দেখান।
    #আপলোড করা ফাইলটি সার্ভারের একটি নির্দিষ্ট ফোল্ডারে সংরক্ষণ করুন।

class FormFile(BaseModel):
    name : Annotated[str, Form()]
    age : Annotated[int, Form()]
    image : Annotated[UploadFile, File()] = None

@app.post('/upload/data/')
async def upload_form_file(data: Annotated[FormFile, Form(), File()]):
    if data.image:
        file_path  = f"E:/FastAPI/form_task/image/image-{random.randrange(1000, 99999)}-{data.image.filename}"
        with open(file_path , 'wb') as f:
            content = await data.image.read()
            f.write(content)

    return {
        'status': 'success',
        'username' : f'{data.name}',
        'age': f'{data.age}',
        'image': f'{data.image.filename}',
        'path': file_path
    } 

 
   



