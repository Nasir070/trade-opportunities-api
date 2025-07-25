from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    assert client.get('/').status_code == 200

def test_health():
    assert client.get('/health').json()['status'] == 'healthy'

def test_analyze_no_key():
    assert client.get('/api/v1/analyze/pharmaceuticals').status_code == 401
