# MindGraph Data Pipeline

This project is a containerized data pipeline setup that integrates **Apache Airflow**, **Apache Spark**, **FastAPI**, **MinIO**, **PostgreSQL**, and **Redis** using **Docker Compose**.  
It automates data extraction, transformation, and storage in a modular and scalable way.

---

## 🧱 Components

| Service | Description |
|----------|-------------|
| **Airflow Webserver** | Manages and visualizes DAG workflows |
| **Airflow Scheduler** | Triggers and manages scheduled DAG executions |
| **PostgreSQL** | Metadata database for Airflow |
| **Redis** | Broker used by Airflow scheduler |
| **MinIO** | Local S3-compatible storage for raw and transformed data |
| **Spark** | Used for data transformation tasks |
| **FastAPI** | Generates and exposes data endpoints for extraction |

---

## 🗂️ Current Directory Structure

```
mindgraph_project/
│
├── airflow_dags/
│   ├── extract_fastapi_dag.py
│   ├── load_to_minio_dag.py
│   ├── phase3_1_spark_transform.py
│   └── scripts/
│       └── phase3_spark_transform.py
│
├── airflow_logs/
│
├── fastapi_app/
│   ├── app.py
│   ├── data_generator.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── spark/
│   └── Dockerfile
│
├── docker-compose.yml
├── Dockerfile
├── minio_data/
├── raw_data/
└── README.md
```

---

## ⚙️ How to Run

1️⃣ **Navigate to the project folder**
```bash
cd ~/Desktop/mindgraph_project
```

2️⃣ **Build and start all services**
```bash
docker-compose up -d --build
```

3️⃣ **Check running containers**
```bash
docker ps
```

---

## 🌐 Service URLs

| Service | URL |
|----------|-----|
| **Airflow Web UI** | http://localhost:8080 |
| **MinIO Console** | http://localhost:9001 |
| **FastAPI Server Full Data Load** | http://localhost:8000/data/full |
<img width="1440" height="900" alt="Screenshot 2025-11-04 at 1 46 44 PM" src="https://github.com/user-attachments/assets/65546596-9bea-4547-a40c-7e88b8f9cb3c" />
<img width="1440" height="900" alt="Screenshot 2025-11-04 at 2 01 49 PM" src="https://github.com/user-attachments/assets/a4645f4d-ac24-4478-9cbb-47e30c28c54e" />

---

## 🧩 Useful Commands

**Stop all containers**
```bash
docker-compose down
```

**Rebuild Spark only**
```bash
docker-compose build --no-cache spark
```

**Run Spark job manually**
```bash
docker exec -it mindgraph_spark bash
spark-submit /opt/airflow/dags/scripts/phase3_spark_transform.py
```

---

## 📦 Environment Variables

| Variable | Default |
|-----------|----------|
| `MINIO_ROOT_USER` | minioadmin |
| `MINIO_ROOT_PASSWORD` | minioadmin |
| `POSTGRES_USER` | airflow |
| `POSTGRES_PASSWORD` | airflow |

---

## ✍️ Author

**Karthick Raja P**  
MSc Data Science | Data Engineer | Azure | PySpark | SQL | ETL Pipelines  
📘 [GitHub: Karthick-P-Raja](https://github.com/Karthick-P-Raja)

---
