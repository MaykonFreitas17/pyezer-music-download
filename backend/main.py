from typing import Union

from fastapi import FastAPI

app = FastAPI()

# URL padrão
URL_DEFAULT = '/api/v1/'

# Routes
@app.get(f'{URL_DEFAULT}')
async def hello_world():
    return {
        "mensage": "Hello World, FastAPI",
        "status": 'OK',
        "code": 200,
    }
    
@app.get(f'{URL_DEFAULT}/video')
async def hello_world():
    return {
        "mensage": "Hello World, FastAPI",
        "state": 'OK',
        "code": 200,
    }