from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MinIO Data Transform").getOrCreate()

print(" Spark transformation script started")

# Example dummy data
data = [("Karthick", "Raja", 1000), ("Data", "Engineer", 2000)]
columns = ["first_name", "last_name", "salary"]

df = spark.createDataFrame(data, columns)
df.show()

print(" Transformation complete")

spark.stop()

