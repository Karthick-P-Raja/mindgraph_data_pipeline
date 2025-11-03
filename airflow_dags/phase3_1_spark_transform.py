from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark Session with MinIO (S3A) configs
spark = SparkSession.builder \
    .appName("MindGraph_Phase3_Transformation") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

# ✅ Step 1: Read raw data from MinIO
raw_df = spark.read.option("header", "true").csv("s3a://raw-data/finance_data.csv")

# ✅ Step 2: Simple transformations (example)
transformed_df = raw_df.withColumn(
    "transaction_amount",
    col("transaction_amount").cast("double")
).withColumn(
    "status",
    when(col("transaction_amount") > 1000, "HIGH").otherwise("LOW")
)

# ✅ Step 3: Write back to MinIO in Parquet format
transformed_df.write.mode("overwrite").parquet("s3a://processed-data/finance_cleaned")

spark.stop()
print("✅ Transformation complete and saved to MinIO!")

