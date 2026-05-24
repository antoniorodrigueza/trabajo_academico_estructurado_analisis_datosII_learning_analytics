import matplotlib
import matplotlib
matplotlib.use('Agg')  # backend compatible con Colab
import matplotlib.pyplot as plt
from IPython.display import display

umbral = 5

def filtrar_bajo_rendimiento(tabla_notas):
    seleccion = tabla_notas[tabla_notas['nota'] < umbral]
    return seleccion

def visualizar_notas(registro):
    plt.figure(figsize=(8, 5))
    plt.bar(registro['nombre'], registro['nota'], color='skyblue')

    # Línea roja en el valor del umbral
    plt.axhline(y=umbral, color='red', linestyle='--', linewidth=2)

    plt.title('Rendimiento Académico')
    plt.xlabel('Alumnado')
    plt.ylabel('Calificación')
    plt.tight_layout()

    # Mostrar explícitamente en Colab
    display(plt.gcf())
    plt.close()
