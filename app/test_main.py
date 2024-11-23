from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_receipt():
    receipt = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"}
        ],
        "total": "18.74"
    }
    response = client.post("/receipts/process", json=receipt)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_points():
    receipt_id = "test-id"
    app.receipts[receipt_id] = 42
    response = client.get(f"/receipts/{receipt_id}/points")
    assert response.status_code == 200
    assert response.json() == {"points": 42}
