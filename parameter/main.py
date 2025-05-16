from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# parameters
@app.get('/user/edit/{id}') 
async def user_edit(id: int): 
    return {
        'status': 'success',
        'message':{
            'id': id,
            'name' : 'shahoraiar'
        }
    }
# multiple path parameter
@app.get('/user/{user_id}/post/{post_name}')
async def get_user_post(user_id: int, post_name: str):
    return {
        'status': 'success',
        'message':{
            'user id': user_id,
            'post_name': post_name
        }
    } 

# query parameters
@app.get('/user/details/')
def user_details(user_id: int, query: dict | None=None) : # query: Optional[str] = None
    if query:
        return{
            'userid ': user_id,
            'query': query
        }
    return {"user id": user_id}


