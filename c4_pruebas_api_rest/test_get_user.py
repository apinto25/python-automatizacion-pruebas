import requests

BASE_URL = "http://127.0.0.1:8000"


def test_user_validation():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data["id"], int)
    assert isinstance(data["username"], str)

    assert "email" in data
    assert "@" in data["email"]


def test_user_validation_not_found():
    response = requests.get(f"{BASE_URL}/users/0")

    assert response.status_code == 404
    assert "detail" in response.json()
    assert response.json()["detail"] == "Usuario no encontrado"
