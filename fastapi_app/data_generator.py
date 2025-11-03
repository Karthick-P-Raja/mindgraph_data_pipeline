import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(n=20, start_id=1):
    base_time = datetime.now() - timedelta(days=5)
    data = []
    for i in range(n):
        record = {
            "transaction_id": start_id + i,
            "timestamp": (base_time + timedelta(minutes=i * 10)).isoformat(),
            "user_id": random.randint(1000, 1010),
            "amount": round(random.uniform(10, 1000), 2),
            "currency": "USD",
            "status": random.choice(["SUCCESS", "FAILED", "PENDING"])
        }
        data.append(record)
    return pd.DataFrame(data)
