from fastapi import FastAPI, HTTPException
from uuid import uuid4
from app.utils import calculate_points

app = FastAPI()
receipts = {}

@app.post("/receipts/process")
async def process_receipt(receipt: dict):
    receipt_id = str(uuid4())
    points = calculate_points(receipt)
    receipts[receipt_id] = points
    return {"id": receipt_id}

@app.get("/receipts/{id}/points")
async def get_points(id: str):
    if id not in receipts:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return {"points": receipts[id]}
