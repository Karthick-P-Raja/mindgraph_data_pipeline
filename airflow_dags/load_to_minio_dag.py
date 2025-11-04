from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3
import os

MINIO_ENDPOINT = "minio:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
MINIO_BUCKET = "raw-data"

RAW_DATA_DIR = "/opt/airflow/raw_data"

def upload_to_minio():
    s3_client = boto3.client(
        "s3",
        endpoint_url=f"http://{MINIO_ENDPOINT}",
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
    )

    try:
        s3_client.head_bucket(Bucket=MINIO_BUCKET)
    except:
        s3_client.create_bucket(Bucket=MINIO_BUCKET)

    for filename in os.listdir(RAW_DATA_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(RAW_DATA_DIR, filename)
            s3_client.upload_file(file_path, MINIO_BUCKET, filename)
            print(f" Uploaded: {filename}")

default_args = {
    'start_date': datetime(2025, 11, 2),
}

with DAG(
    dag_id='load_to_minio_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['mindgraph']
) as dag:

    upload_task = PythonOperator(
        task_id='upload_to_minio',
        python_callable=upload_to_minio
    )

    upload_task
