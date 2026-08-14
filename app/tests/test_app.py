import pytest
import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    data = json.loads(res.data)
    assert "message" in data

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data['status'] == 'healthy'

def test_ready(client):
    res = client.get('/ready')
    assert res.status_code == 200

def test_tasks(client):
    res = client.get('/tasks')
    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data) > 0