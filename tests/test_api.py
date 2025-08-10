# tests/test_api.py

from fastapi.testclient import TestClient
from app.main import app  # Adjust import based on your project structure

client = TestClient(app)

def test_predict_endpoint_valid_input():
    sample_data = {
    "island": 0,
    "bill_length_mm": 39.1,
    "bill_depth_mm": 18.7,
    "flipper_length_mm": 181.0,
    "body_mass_g": 3750.0,
    "sex": 1,
    "year": 2007
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "predicted_species" in response.json()
def test_predict_missing_field():
    sample_data = {
        "island": 0,
        # "bill_length_mm" missing here
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181.0,
        "body_mass_g": 3750.0,
        "sex": 1,
        "year": 2007
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422  # Unprocessable Entity due to validation error
def test_predict_invalid_type():
    sample_data = {
        "island": 0,
        "bill_length_mm": "thirty-nine",  # Invalid string instead of float
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181.0,
        "body_mass_g": 3750.0,
        "sex": 1,
        "year": 2007
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422
def test_predict_out_of_range_value():
    sample_data = {
        "island": 0,
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181.0,
        "body_mass_g": -100,  # Negative body mass
        "sex": 1,
        "year": 2007
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
def test_predict_empty_request():
    response = client.post("/predict", json={})
    assert response.status_code == 422

