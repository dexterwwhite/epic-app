# tests/test_app.py
import pytest
from app import createApp

"""
FOR LOCAL TESTING:

Run with python3 -m pytest
OR
Make sure export PYTHONPATH=. and then use pytest

Running pytest alone was giving me a ModuleNotFoundError
"""

@pytest.fixture
def client():
    app = createApp()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_testEndpoint(client):
    """Testing the test endpoint"""
    response = client.get('/test')
    data = response.get_json()

    assert response.status_code == 200
    assert "User" in data
    assert "Config Variable" in data
    assert "Sub-Map" in data
    assert data["Sub-Map"]["Key4"] == "TEST"
