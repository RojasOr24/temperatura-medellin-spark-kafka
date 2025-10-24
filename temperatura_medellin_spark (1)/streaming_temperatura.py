from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder.appName("StreamingTemperaturaMedellin").getOrCreate()

schema = StructType()     .add("date", StringType())     .add("tempmax", DoubleType())     .add("tempmin", DoubleType())     .add("temp", DoubleType())

df_stream = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "clima_medellin")     .load()

valores = df_stream.selectExpr("CAST(value AS STRING)")
datos = valores.select(from_json(col("value"), schema).alias("data")).select("data.*")

promedio_stream = datos.groupBy().agg(avg("temp").alias("promedio_temp"))

consulta = promedio_stream.writeStream     .outputMode("complete")     .format("console")     .start()

consulta.awaitTermination()
