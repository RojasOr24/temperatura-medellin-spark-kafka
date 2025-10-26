# se crean Spark , para la ejecucion de DataFrame y SQL en PYsPARK.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min

spark = SparkSession.builder.appName("TemperaturaMedellinBatch").getOrCreate()
#se carga los datos 
data_path = "historical-weather-medellin.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)
#muestra muestra la estructura y se verifica que los datos se leen correctamente
print("  Esquema de datos:")
df.printSchema()

print("  Muestra de datos:")
df.show(5)
#se limpian los datos y se eliminan los valores nulos
df_clean = df.select("date", "tempmax", "tempmin", "temp").dropna()
#se calcula los valores agregados en el conjunto de datos
stats = df_clean.agg(
    avg("tempmax").alias("promedio_max"),
    avg("tempmin").alias("promedio_min"),
    avg("temp").alias("promedio_general"),
    max("tempmax").alias("temperatura_maxima"),
    min("tempmin").alias("temperatura_minima")
)

print("  Estadísticas generales de temperatura:")
stats.show() #muestra las estadisticas calculadas
stats.write.mode("overwrite").csv("resultados_temperatura_batch/") #guarda los resultados en la carpeta
print("  Resultados guardados en carpeta: resultados_temperatura_batch/") #detalle el resultado

