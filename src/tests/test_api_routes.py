from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_simulation_taxi_endpoint_success():
    payload = {
        "alpha": 0.8,
        "gamma": 0.95,
        "epsilon": 1.0,
        "epsilon_decay": 0.9995,
        "epsilon_min": 0.01,
        "num_episodes": 10
    }
    response = client.post("/api/taxi", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "success_rate" in data
    assert "path" in data

def test_simulation_invalid_alpha_returns_validation_error():
    # Envia alpha = 2.0 (o limite do Pydantic é 1.0)
    payload = {
        "alpha": 2.0,
        "gamma": 0.95,
        "epsilon": 1.0,
        "epsilon_decay": 0.9995,
        "epsilon_min": 0.01,
        "num_episodes": 10
    }
    response = client.post("/api/taxi", json=payload)
    assert response.status_code == 422  # Unprocessable Entity