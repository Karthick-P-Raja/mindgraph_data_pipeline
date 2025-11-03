from fastapi import FastAPI, Query
from data_generator import generate_data
import json

app = FastAPI(title="Finance Data API", version="1.0")

full_data = generate_data(30)

@app.get("/data/full")
def get_full_data():
    """Returns all transactions (Day 0 load)"""
    return json.loads(full_data.to_json(orient="records"))

@app.get("/data/incremental")
def get_incremental(after_id: int = Query(0, description="Fetch records after this transaction ID")):
    """Returns incremental data (new transactions)"""
    filtered = full_data[full_data["transaction_id"] > after_id]
    return json.loads(filtered.to_json(orient="records"))
