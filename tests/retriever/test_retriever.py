from src.retriever import get_similar_responses

def test_get_similar_responses():
    assert get_similar_responses("What is the capital of France?") == ["These are test responses"]
    
    
    
    q = "What is the capital of France?"
    
    
    # Tests for the retriever
    
    result = get_similar_responses(question = q, top_k=5)
    
    # Ensure that the length of the response is 10
    assert len(result) == 5
    
    # Ensure that the result is a list
    assert isinstance(result, list)
    


