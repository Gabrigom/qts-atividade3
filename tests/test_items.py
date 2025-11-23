from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_item_sucesso():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Item 1"}
    
def test_get_item_nao_encontrado():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Cartão Inválido"}