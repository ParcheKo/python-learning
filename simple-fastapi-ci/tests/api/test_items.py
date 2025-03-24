from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Book", "description": "A novel"})
    assert response.status_code == 200
    assert response.json()["name"] == "Book"

def test_list_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0