from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='phase3_spark_transform_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['spark', 'minio', 'transform']
) as dag:

    run_spark_transformation = BashOperator(
        task_id='run_spark_transformation',
        bash_command='docker exec mindgraph_spark /opt/spark/bin/spark-submit /opt/airflow/dags/scripts/spark_transform_script.py'
    )

    run_spark_transformation

