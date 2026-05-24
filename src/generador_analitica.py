import matplotlib
matplotlib.use('Agg')  # backend compatible
import matplotlib.pyplot as plt
from IPython.display import display


def filtrar_bajo_rendimiento(tabla_notas):
    umbral = 5
    seleccion = tabla_notas[tabla_notas['nota'] < umbral]
    return seleccion

def visualizar_notas(registro):
    plt.figure(figsize=(8, 5))
    plt.bar(registro['nombre'], registro['nota'], color='skyblue')
    plt.title('Rendimiento Académico')
    plt.xlabel('Alumnado')
    plt.ylabel('Calificación')
    plt.tight_layout()

    # Mostrar explícitamente en Colab
    display(plt.gcf())
    plt.close()
