from kafka import KafkaProducer
import pandas as pd
import json, time

df = pd.read_csv("historical-weather-medellin.csv")

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Enviando datos a Kafka topic: clima_medellin")

for _, row in df.iterrows():
    mensaje = {
        "date": str(row["date"]),
        "tempmax": float(row["tempmax"]),
        "tempmin": float(row["tempmin"]),
        "temp": float(row["temp"])
    }
    producer.send("clima_medellin", value=mensaje)
    print(f"✅ Enviado: {mensaje}")
    time.sleep(1)
