# Receipt Processor Challenge

## Overview

This project implements a receipt processing web service as described in the [Fetch Rewards Receipt Processor Challenge](https://github.com/fetch-rewards/receipt-processor-challenge). The API includes two endpoints:

- **Process Receipts (`POST /receipts/process`)**: Accepts a receipt JSON, calculates points based on predefined rules, and returns a unique ID for the receipt.
- **Get Points (`GET /receipts/{id}/points`)**: Retrieves the points awarded for a receipt using its ID.

## Features

- In-memory data storage (no external database required).
- Rules-based points calculation.
- Fully containerized using Docker.
- Unit tests included for core functionality.

---

## API Endpoints

### Process Receipts

- **Path**: `/receipts/process`
- **Method**: `POST`
- **Description**: Accepts a receipt in JSON format, calculates the points, and returns a unique receipt ID.

**Example Request**:

```json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },
    {
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    }
  ],
  "total": "18.74"
}
```

**Example Response**:

```json
{
  "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
}
```

### Get Points

- **Path**: `/receipts/{id}/points`
- **Method**: `GET`
- **Description**: Retrieves the points awarded to a receipt by its unique ID.

**Example Response**:

```json
{
  "points": 32
}
```

## Installation and Usage

### Local Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd receipt-processor-challenge
   ```

2. **Create a virtual environment and activate it**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
   ```

   The service will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Docker Setup

1. **Build and run the Docker container**:

   ```bash
   docker-compose up --build
   ```

   The service will be available at [http://localhost:8000](http://localhost:8000).

## Rules for Points Calculation

- **Retailer Name**:

  - 1 point for every alphanumeric character.

- **Total Amount**:

  - 50 points if the total is a round dollar amount.
  - 25 points if the total is a multiple of 0.25.

- **Items**:

  - 5 points for every two items.
  - If the trimmed length of an item description is a multiple of 3, multiply the item's price by 0.2 and round up to the nearest integer to calculate additional points.

- **Purchase Date**:

  - 6 points if the day is odd.

- **Purchase Time**:
  - 10 points if the time is between 2:00 PM and 4:00 PM.

## Testing

1. **Run Unit Tests**:

   ```bash
   pytest
   ```

## Example Usage

### Process a Receipt

```bash
curl -X POST "http://127.0.0.1:8000/receipts/process" \
-H "Content-Type: application/json" \
-d '{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
    {"shortDescription": "Emils Cheese Pizza", "price": "12.25"}
  ],
  "total": "18.74"
}'
```

### Get Points for a Receipt

```bash
curl -X GET "http://127.0.0.1:8000/receipts/<receipt-id>/points"
```

Replace `<receipt-id>` with the ID returned from the `/receipts/process` endpoint.

## Files and Structure

```
receipt-processor-challenge/
├── app/
│   ├── __init__.py
│   ├── main.py          # API endpoints
│   ├── models.py        # Data models (if required)
│   ├── utils.py         # Points calculation logic
│   └── test_main.py     # Unit tests
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

## Dependencies

- **Python 3.9 or later**
- **FastAPI**
- **Uvicorn**
- **Docker** (optional)
- **pytest** (for testing)
