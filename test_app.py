"""Tests for two tier flask application."""
from unittest.mock import patch, MagicMock
from app import app

def test_health():
    """Test health endpoint returns 200."""
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200

def test_hello():
    """Test hello endpoint returns 200 with mocked DB."""
    with patch('app.mysql') as mock_mysql:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('hello',), ('world',)]
        mock_mysql.connection.cursor.return_value = mock_cursor

        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200

def test_submit():
    """Test submit endpoint returns 200 with mocked DB."""
    with patch('app.mysql') as mock_mysql:
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        client = app.test_client()
        response = client.post('/submit', data={'new_message': 'test message'})
        assert response.status_code == 200
