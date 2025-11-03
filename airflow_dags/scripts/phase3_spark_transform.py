from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, avg

spark = (
    SparkSession.builder
    .appName("Phase3SparkTransformation")
    .config("spark.hadoop.fs.s3a.endpoint", "http://mindgraph_minio:9000")
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin")
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
    .getOrCreate()
)

print("✅ Spark connected to MinIO")

input_path = "s3a://finance-bucket/raw/finance_raw.csv"
output_path = "s3a://finance-bucket/processed/finance_transformed/"

df = spark.read.option("header", True).csv(input_path)
df_transformed = (
    df.withColumn("amount", col("amount").cast("double"))
      .withColumn("status_flag", when(col("amount") > 5000, lit("High")).otherwise(lit("Normal")))
)

df_summary = df_transformed.groupBy("status_flag").agg(avg("amount").alias("avg_amount"))
df_summary.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

spark.stop()
print("✅ Transformation complete")
