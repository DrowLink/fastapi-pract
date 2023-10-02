from typing import Union
from fastapi import FastAPI
from models.item_model import Item

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/calculator")
def calcular(valor1: float, valor2: float):
    return {"suma": valor1 + valor2}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}