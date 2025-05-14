from fastapi.testclient import TestClient
from src.main import app
from src.utils.helpers import data_loader

client = TestClient(app)

def test_query_endpoint():
    
    response = client.post("/similar_responses", json={"question": "What is the capital of France?"})
    assert response.status_code == 200
    
    # Extra tests
    assert 
    
    assert response.json() == {"answers": ["These are test responses"]}
