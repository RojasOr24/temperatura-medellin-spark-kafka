from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg
from pyspark.sql.types import StructType, StringType, DoubleType
#se crea la sesion Spark Streaming
spark = SparkSession.builder.appName("StreamingTemperaturaMedellin").getOrCreate()
#se define el esquema de los mensales JSON, es decir el formato de los datos que envia Kafka
schema = StructType()     .add("date", StringType())     .add("tempmax", DoubleType())     .add("tempmin", DoubleType())     .add("temp", DoubleType())
#lee los datos de Kafka
df_stream = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "clima_medellin")     .load()
#extrae y convierte los valores a texto y se define el esquema
valores = df_stream.selectExpr("CAST(value AS STRING)")
datos = valores.select(from_json(col("value"), schema).alias("data")).select("data.*")
#calcula el promedio en tiempo real 
promedio_stream = datos.groupBy().agg(avg("temp").alias("promedio_temp"))
#Imprime el resultado cada vez que cambia el promedio
consulta = promedio_stream.writeStream     .outputMode("complete")     .format("console")     .start()

consulta.awaitTermination()
