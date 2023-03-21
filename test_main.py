"""
Test goes here

"""

import pytest
from starlette.testclient import TestClient
from main import app

@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client
    
def test_index(client):
   res = client.get('/')
   assert res.status_code == 200
