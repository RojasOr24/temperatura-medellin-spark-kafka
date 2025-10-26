#se importan las librerias necesarias
from kafka import KafkaProducer
import pandas as pd
import json, time
#lee los datos historicos
df = pd.read_csv("historical-weather-medellin.csv")
#indica donde se encuentra el kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print(" Enviando datos a Kafka topic: clima_medellin")
#envia los datos topic
for _, row in df.iterrows():
    mensaje = {
        "date": str(row["date"]),
        "tempmax": float(row["tempmax"]),
        "tempmin": float(row["tempmin"]),
        "temp": float(row["temp"])
    }
    producer.send("clima_medellin", value=mensaje)
    print(f"  Enviado: {mensaje}")
    time.sleep(1)
