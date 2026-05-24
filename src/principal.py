import sys
sys.path.append('/content/trabajo_academico_estructurado_analisis_datosII_learning_analytics/src')

from cargador_de_datos import cargar_dataset as cargar_archivo
from cifrador import codificar_texto as cifrar_texto, descodificar_texto as descifrar_texto
from generador_blockchain import CadenaBloques as CadenaSegura
from generador_analitica import filtrar_bajo_rendimiento as filtrar_riesgo, visualizar_notas as graficar_notas


def main():
    # --- Lectura del dataset ---
    tabla_estudiantes = cargar_archivo('data/estudiantes.csv')
    
    # --- Cifrado de nombres ---
    print('\n >> Cifrado de nombres')
    tabla_estudiantes['nombre_cifrado'] = tabla_estudiantes['nombre'].apply(cifrar_texto)
    print(tabla_estudiantes[['nombre', 'nombre_cifrado']])
    
    # --- Registro en Blockchain ---
    print('\n >> Registro en Blockchain')
    cadena = CadenaSegura()
    
    for _, fila in tabla_estudiantes.iterrows():
        paquete = {'alumno': fila['nombre'], 'nota': fila['nota']}
        cadena.insertar_bloque(paquete)
    
    # --- Verificacion de la cadena de blockchain
    print('\n >> Verificacion de la cadena. ¿Es una cadena íntegra?:', cadena.validar_cadena())

    
    # --- Análisis de riesgo ---
    grupo_riesgo = filtrar_riesgo(tabla_estudiantes)
    print('\n >> Listado de estudiantes en riesgo:\n', grupo_riesgo)
    
    # --- Verificacion de la tabla estudiante y estructura
    print('\n >> Verificacion de la tabla estudiante y estructura:')
    print(tabla_estudiantes.columns)
    
    # --- Visualización de los estudiantes
    print('\n >> Visualizacion de los estudiantes\n')
    graficar_notas(tabla_estudiantes)

if __name__ == '__main__':
    main()
