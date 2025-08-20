from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ping():
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_sum():
    resp = client.post("/sum", json={"numbers": [1, 2, 3]})
    assert resp.status_code == 200
    assert resp.json()["sum"] == 6.0
