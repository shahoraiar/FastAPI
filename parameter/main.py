from fastapi import FastAPI, Path, Query, Body
from typing import Optional, List
from pydantic import BaseModel

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

# path parameter numeric validation
@app.get("/read/items/{item_id}")
def read_item_validation(
    item_id: int = Path(title="Read Item ID", description="The ID must be between 1 and 1000", ge=1, le=1000)
):
    return {"item_id": item_id}

# query parameters
@app.get('/user/details/')
def user_details(user_id: int, search: str | None = None, sort: bool = False) : # query: Optional[str] = None
    if search:
        return{
            'userid ': user_id,
            'query': search,
            'sort' : sort 
        }
    return {"user id": user_id, "sort":sort}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(start: int = 0, limit: int = 10):
    return fake_items_db[start : start + limit]


@app.get("/user/{user_id}")
def get_user_both_parameter(user_id: int = Path(..., ge=1), search: str = Query(None)):
    return {
        "user_id": user_id,
        "search": search
    }


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/create/items/")
async def create_item(item: Item):
    print('create item')
    print('item : ', item) 
    return item


@app.post("/login/")
def login(username: str = Body(...), password: str = Body(...)):
    print('username : ', username, '|| passoword : ', password)
    return {"username": username}



