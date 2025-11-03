from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="phase3_spark_transform_dag",
    start_date=datetime(2025, 11, 3),
    schedule_interval=None,
    catchup=False,
    tags=["mindgraph"]
) as dag:

    spark_transform = BashOperator(
        task_id="run_spark_transformation",
        bash_command=(
            "docker exec mindgraph_spark "
            "spark-submit /opt/airflow/dags/phase3_1_spark_transform.py"
        )
    )

    spark_transform
