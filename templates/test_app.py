import pytest
from app import app  # assumes app.py defines `app = Flask(__name__)`

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data or b"Hello" in response.data

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data

def test_404_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
