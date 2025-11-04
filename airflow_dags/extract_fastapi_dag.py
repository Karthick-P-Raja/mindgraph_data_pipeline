from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import json
import os

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

def extract_data():
    url = "http://fastapi:8000/data/full"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        os.makedirs("/opt/airflow/raw_data", exist_ok=True)
        filename = f"/opt/airflow/raw_data/full_load_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Data successfully saved to: {filename}")

    except Exception as e:
        print(f" Failed to extract data from FastAPI: {e}")
        raise

with DAG(
    dag_id="extract_fastapi_dag",
    default_args=default_args,
    description="Extracts data from FastAPI and stores locally",
    schedule_interval="@daily",
    start_date=datetime(2025, 11, 1),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_fastapi_data",
        python_callable=extract_data
    )
