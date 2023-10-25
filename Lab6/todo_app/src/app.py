from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

items_db = {}

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/items/{item_id}/")
async def read_item_filter(item_id: int, name_contains: Optional[str] = None):
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if name_contains:
        if name_contains.lower() in item['name'].lower():
            return item
        else:
            raise HTTPException(status_code=404, detail=f"No item with ID {item_id} contains the name '{name_contains}'")
    
    return item

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    items = list(items_db.values())[skip : skip + limit]
    return items

@app.post("/items/")
async def create_item(item: dict):
    item_id = len(items_db) + 1
    items_db[item_id] = item
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}
