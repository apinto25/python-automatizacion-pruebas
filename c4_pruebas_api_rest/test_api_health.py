import requests

BASE_URL = "http://127.0.0.1:8000"

def test_api_health():
    response = requests.get(f"{BASE_URL}/health")
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "ok"
