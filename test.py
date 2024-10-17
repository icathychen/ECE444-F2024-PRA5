import pytest
from application import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_fake_news(client):
    fake_news_inputs = [
        "This is a hoax and a scam!",
        "Unbelievable clickbait story!"
    ]
    for news in fake_news_inputs:
        response = client.post("/", data={"input_text": news})
        assert b"FAKE" in response.data 
     

def test_real_news(client):
    real_news_inputs = [
        "This is a real news",
        "The govenment has just pass a new law"
    ]
    for news in real_news_inputs:
        response = client.post("/", data={"input_text": news})
        assert b"REAL" in response.data 
    
    