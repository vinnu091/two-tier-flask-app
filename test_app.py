"""Tests for two tier flask application."""
from app import app

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
