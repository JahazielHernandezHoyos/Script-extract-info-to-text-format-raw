import pandas as pd
import numpy as np

DATE = "06/07/2019"
consecutivo = 1


def extraer_datos():
    """
    📤 Esta función extrae los datos de un archivo de texto con formato fijo y los guarda en un archivo CSV.
    Los datos extraídos incluyen la marca, tipo, ubicación y placa de vehículos, así como la fecha y un número consecutivo.
    El archivo de texto debe tener las siguientes dimensiones:
    - La primera columna debe tener una longitud de 20 caracteres y corresponder a la marca del vehículo.
    - La segunda columna debe tener una longitud de 23 caracteres y corresponder al tipo del vehículo.
    - La tercera columna debe tener una longitud de 28 caracteres y corresponder a la ubicación del vehículo.
    - La cuarta columna debe tener una longitud de 5 caracteres y corresponder a la placa del vehículo.
    La función utiliza las variables DATE y consecutivo definidas previamente en el archivo.
    """
    df = pd.read_fwf(
        "prueba_txt.txt",
        widths=[20, 23, 28, 5],
        names=["marca", "tipo", "ubicación", "placa"],
        dtype={"placa": str},
        encoding="ISO-8859-1",
    )

    df["fecha"] = DATE
    df["consecutivo"] = np.arange(consecutivo, consecutivo + len(df))

    df.to_csv("output.csv", index=False)


if __name__ == "__main__":
    extraer_datos()
