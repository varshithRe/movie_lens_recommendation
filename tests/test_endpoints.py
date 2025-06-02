import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert data.get('status') == 'up'

def test_recommend_endpoint_valid():

    response = client.post('/recommend', json = {'user_id': 3}) #omotting n to see if it gets 10 titles
    assert response.status_code == 200
    data = response.json()
    assert 'recommendations' in data
    recs = data['recommendations']
    assert isinstance(recs, list)
    assert len(recs) == 10

def test_recommend_end_point_invalid_user():
    response = client.post('/recommend', json = {'user_id': 775219875})

    assert response.status_code == 404

def test_similar_end_point_valid():
    response = client.post('/similar', json = {'item': 'Godfather'})
    assert response.status_code == 200
    data = response.json()
    assert 'recommendations' in data
    recs = data['recommendations']
    assert isinstance(recs, list)
    assert len(recs) ==  6

def test_similar_end_point_invalid_user():
    response = client.post('/similar', json = {'item': 'no_movie'})

    assert response.status_code == 404
