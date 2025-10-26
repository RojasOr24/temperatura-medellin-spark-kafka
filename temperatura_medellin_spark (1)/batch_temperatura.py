from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min

spark = SparkSession.builder.appName("TemperaturaMedellinBatch").getOrCreate()
data_path = "historical-weather-medellin.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

print("  Esquema de datos:")
df.printSchema()

print("  Muestra de datos:")
df.show(5)

df_clean = df.select("date", "tempmax", "tempmin", "temp").dropna()

stats = df_clean.agg(
    avg("tempmax").alias("promedio_max"),
    avg("tempmin").alias("promedio_min"),
    avg("temp").alias("promedio_general"),
    max("tempmax").alias("temperatura_maxima"),
    min("tempmin").alias("temperatura_minima")
)

print("  Estadísticas generales de temperatura:")
stats.show()
stats.write.mode("overwrite").csv("resultados_temperatura_batch/")
print("  Resultados guardados en carpeta: resultados_temperatura_batch/")

