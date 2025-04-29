from src.services.ml_service import predict

def test_predict():
    assert predict([1, 2, 3]) == 2.0
