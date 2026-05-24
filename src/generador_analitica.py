import pandas as pd
import matplotlib.pyplot as plt


def filtrar_bajo_rendimiento(tabla_notas):
    umbral = 5
    seleccion = tabla_notas[tabla_notas['grade'] < umbral]
    return seleccion


def visualizar_notas(registro):
    plt.figure(figsize=(8, 5))
    nombres = registro['name']
    valores = registro['grade']

    plt.bar(nombres, valores, color='skyblue')
    plt.title('Rendimiento Académico')
    plt.xlabel('Alumnado')
    plt.ylabel('Calificación')
    plt.tight_layout()
    plt.show()

