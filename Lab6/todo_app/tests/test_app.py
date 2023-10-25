from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_read_item():
    item = {"name": "item1", "description": "test item"}
    response = client.post("/items/", json=item)
    assert response.status_code == 200
    
    item_id = 1
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == item

def test_read_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404

def test_read_item_filter_name_contains():
    item_id = 1
    response = client.get(f"/items/{item_id}/", params={"name_contains": "item"})
    assert response.status_code == 200

    item_id = 999
    response = client.get(f"/items/{item_id}/", params={"name_contains": "item"})
    assert response.status_code == 404

    item_id = 1
    response = client.get(f"/items/{item_id}/", params={"name_contains": "item"})
    assert response.status_code == 200
    
    item_id = 1
    response = client.get(f"/items/{item_id}/", params={"name_contains": "nonexistent"})
    assert response.status_code == 404
    assert response.json() == {"detail": f"No item with ID {item_id} contains the name 'nonexistent'"}

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_item():
    item_id = 1
    updated_item = {"name": "updated", "description": "updated item"}
    response = client.put(f"/items/{item_id}", json=updated_item)
    assert response.status_code == 200
    assert response.json() == updated_item

def test_delete_item():
    item_id = 1
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}
