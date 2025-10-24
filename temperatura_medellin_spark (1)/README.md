# 🌡️ Análisis de Temperatura en Medellín con Apache Spark y Kafka

Este proyecto implementa procesamiento **batch** y **en tiempo real** de datos históricos de temperatura usando **Apache Spark** y **Apache Kafka**, como parte de la Tarea 3 del curso **Big Data – UNAD**.

## 📂 Estructura del proyecto
```
temperatura_medellin_spark/
├── historical-weather-medellin.csv
├── batch_temperatura.py
├── productor_temperatura.py
├── streaming_temperatura.py
└── README.md
```

## ⚙️ Requisitos
- Python 3.8+
- Apache Spark 3.5
- Apache Kafka 3.7
- Paquetes: `pyspark`, `pandas`, `kafka-python`

## 🚀 Ejecución

### 🔸 Procesamiento batch
```bash
python3 batch_temperatura.py
```

### 🔸 Kafka – Envío de datos
1. Iniciar Zookeeper y Kafka:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties
   ```
2. Crear topic:
   ```bash
   bin/kafka-topics.sh --create --topic clima_medellin --bootstrap-server localhost:9092
   ```
3. Ejecutar productor:
   ```bash
   python3 productor_temperatura.py
   ```

### 🔸 Procesamiento en streaming
```bash
python3 streaming_temperatura.py
```

## 🧠 Resultados esperados
- Estadísticas de temperatura promedio, máxima y mínima (batch).  
- Cálculo de temperatura promedio en tiempo real (streaming).  

### 📚 Autora
**Lindi Yureidy Rojas**  
Universidad Nacional Abierta y a Distancia – UNAD  
Curso: *Big Data* (Tarea 3 – Procesamiento de Datos con Apache Spark)
