from cargador_de_datos import cargar_dataset as cargar_archivo
from cifrador import codificar_texto as cifrar_texto, descodificar_texto as descifrar_texto
from generador_blockchain import CadenaBloques as CadenaSegura
from generador_analitica import filtrar_bajo_rendimiento as filtrar_riesgo, visualizar_notas as graficar_notas

# --- Lectura del dataset ---
tabla_estudiantes = cargar_archivo('../data/estudiantes.csv')

# --- Cifrado de nombres ---
tabla_estudiantes['nombre_cifrado'] = tabla_estudiantes['name'].apply(cifrar_texto)
print(tabla_estudiantes[['name', 'nombre_cifrado']])

# --- Registro en Blockchain ---
cadena = CadenaSegura()

for _, fila in tabla_estudiantes.iterrows():
    paquete = {
        'alumno': fila['name'],
        'calificacion': fila['grade']
    }
    cadena.add_block(paquete)
print('¿Cadena íntegra?:', cadena.is_chain_valid())

# --- Análisis de riesgo ---
grupo_riesgo = filtrar_riesgo(tabla_estudiantes)

print('\nListado de estudiantes en riesgo:\n')
print(grupo_riesgo)

# --- Visualización ---
graficar_notas(tabla_estudiantes)
