from fastapi import FastAPI
from first_practice.country import bangladesh

app = FastAPI()
app.include_router(bangladesh.routers, prefix="/country")

@app.get('/')
async def root():
    return {
        'status': 'success',
        'message': 'Hello, FastAPI'
        }

@app.get('/about')
async def about():
    response = {
        'status': 'success',
        'data':{
            'name' : 'My API',
            'age' : 35
        }
    }
    return response

@app.get('/contact')
async def contact():
    response = {
        'status': 'success', 
        'data': {
            'name': "Md Shahoraiar Hossain ",
            'whatsapp': "+8801739-935012",
            'email': 'shahoraiar2000@gmail.com'
        }
    }
    return response

@app.get('/version')
async def version():
    response = {
        'status': 'success',
        'version': 1.0
    }
    return response

@app.get('/query')
async def query(name: str, age: int):
    print(name, age)
    print('ex done')
    return {
        'status': 'success',
        'message': {
            'name': name,
            'age': age
        }
    }
  


