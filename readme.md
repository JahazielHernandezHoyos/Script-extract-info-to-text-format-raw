# 🚗 Script de extracción de datos de vehículos
Este proyecto tiene como objetivo extraer información de vehículos de un archivo de texto con formato fijo y guardarla en un archivo CSV con columnas adicionales de fecha y número consecutivo.

# 📝 Descripción del archivo de texto
El archivo de texto debe tener las siguientes dimensiones:

La primera columna debe tener una longitud de 20 caracteres y corresponder a la marca del vehículo.
La segunda columna debe tener una longitud de 23 caracteres y corresponder al tipo del vehículo.
La tercera columna debe tener una longitud de 28 caracteres y corresponder a la ubicación del vehículo.
La cuarta columna debe tener una longitud de 5 caracteres y corresponder a la placa del vehículo.
# 📦 Dependencias
El Script utiliza las siguientes dependencias:

pandas para leer el archivo de texto y escribir el archivo CSV.
numpy para generar el número consecutivo de transacción.
# 🚀 Cómo ejecutar el Script
Para ejecutar el Script, sigue estos pasos:

Clona el repositorio en tu máquina local.
Abre una terminal en la carpeta del Script.
Ejecuta el siguiente comando: python app.py
El archivo CSV resultante se guardará en la misma carpeta con el nombre output.csv.