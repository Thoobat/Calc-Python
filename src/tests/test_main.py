from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_add():
    res = client.get("/add?a=5&b=3")
    assert res.status_code == 200
    assert res.json() == {"result": 8}

def test_subtract():
    res = client.get("/subtract?a=10&b=4")
    assert res.status_code == 200
    assert res.json() == {"result": 6}

def test_multiply():
    res = client.get("/multiply?a=2&b=3")
    assert res.status_code == 200
    assert res.json() == {"result": 6}

def test_divide():
    res = client.get("/divide?a=10&b=2")
    assert res.status_code == 200
    assert res.json() == {"result": 5}

def test_power():
    res = client.get("/power?a=2&b=3")
    assert res.status_code == 200
    assert res.json() == {"result": 8}

def test_modulo():
    res = client.get("/modulo?a=10&b=3")
    assert res.status_code == 200
    assert res.json() == {"result": 1}

def test_average():
    res = client.get("/average?a=4&b=6")
    assert res.status_code == 200
    assert res.json() == {"result": 5}
