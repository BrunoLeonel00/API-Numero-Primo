from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rota_proximo_primo():
    response = client.get("/entrada/8")
    assert response.status_code == 200
    data = response.json()
    assert data["entrada"] == 8
    assert data["proximo_primo"] == 11

    

