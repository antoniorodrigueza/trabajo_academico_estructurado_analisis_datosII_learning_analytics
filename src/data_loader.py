import pandas as pd

def cargar_dataset(ruta_archivo):
    tabla = pd.read_csv(ruta_archivo)
    return tabla

