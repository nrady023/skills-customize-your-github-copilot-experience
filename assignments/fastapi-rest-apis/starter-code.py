# Starter Code for FastAPI REST API Assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

items = []

# TODO: Add an endpoint to list all items
# @app.get("/items")
# def read_items():
#     ...

# TODO: Add an endpoint to create a new item
# @app.post("/items")
# def create_item(item: Item):
#     ...

# TODO: Add an endpoint to read an item by ID
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     ...

# TODO: Add an endpoint to update an item by ID
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     ...

# TODO: Add error handling for missing items
#     raise HTTPException(status_code=404, detail="Item not found")
