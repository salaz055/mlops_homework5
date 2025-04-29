from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={"features": [1.0, 2.0, 3.0]})
    assert response.status_code == 200
    assert response.json()["prediction"] == 2.0
