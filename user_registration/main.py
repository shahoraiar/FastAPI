from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr, constr
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

fake_users_db = []

class Address(BaseModel):
    city : str | None = None
    zip : int | None = None


class UserIn(BaseModel):
    name : str
    email : EmailStr
    # password : constr(min_length=6)
    password : str
    address : Address

class UserOut(BaseModel):
    name : str
    email : str
    address : Address

app = FastAPI()

# @app.post('/signup/',  response_model=UserOut, response_model_exclude={"password"})
@app.post('/signup/')
async def signup(user: UserIn):
    user_out = UserOut(**user.dict()) # or user.dict(exclude={"password"}) 
    if len(user.password) < 6:
        return JSONResponse({
            'message': 'Password Should At Least 6 Character'
        }, status_code = status.HTTP_400_BAD_REQUEST)
    
    for fake_user in fake_users_db:
        if user.email in fake_user['email']:
            return JSONResponse({
                'message' : 'Email already exists'
            }, status_code=status.HTTP_400_BAD_REQUEST)
        
    fake_users_db.append(user.dict())
    # show_user()
    return JSONResponse({
        'message': "User registered successfully!",
        'user': jsonable_encoder(user_out)
    }, status_code = status.HTTP_201_CREATED)
    # return user

def show_user():
    for user in fake_users_db:
        print('user in db: ', user)

