from src.retriever import get_similar_responses

def test_get_similar_responses():
    assert get_similar_responses("What is the capital of France?") == ["These are test responses"]
    
    
    
    q = "What is the capital of France?"
    # Assert that the top 5 responses are returned
    result = get_similar_responses(question = q, top_k=5)
    assert len(result) == 5
    


