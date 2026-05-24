import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ============================
# 1. Dataset inventado
# ============================
print ('\n >> 1. Dataset inventado\n')
datos = {
    'nombre': ['Ana', 'Luis', 'Marta', 'Pedro', 'Sofía', 'Carlos', 'Elena', 'Jorge'],
    'nota': [4, 7, 3, 9, 5, 6, 8, 2],
    'participacion': [60, 85, 40, 95, 70, 80, 90, 30]
}

df = pd.DataFrame(datos)
print(df)

# ============================
# 2. Preparación de variables
# ============================

print ('\n >> 2. Preparación de variables')
# Característica: participación
caracteristicas = df[['participacion']]
print ('\n >> 2.1. Característica: participación')
print(caracteristicas)

# Objetivo: 1 si suspende (<6), 0 si aprueba
objetivo = (df['nota'] < 6).astype(int)
print ('\n >> Objetivo: 1 si suspende (<6), 0 si aprueba')
print(objetivo)

# ============================
# 3. División del dataset
# ============================
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    caracteristicas,
    objetivo,
    test_size=0.25,
    random_state=42
)
print ('\n >> 3. División del dataset\n')

# ============================
# 4. Modelo
# ============================
clasificador = LogisticRegression()
clasificador.fit(x_entrenamiento, y_entrenamiento)
print ('\n >> 4. Modelo\n')

# ============================
# 5. Predicciones
# ============================
etiquetas_predichas = clasificador.predict(x_prueba)
print ('\n >> 5. Predicciones\n')

# ============================
# 6. Métrica
# ============================
precision = accuracy_score(y_prueba, etiquetas_predichas)
print ('\n >> 6. Métrica\n')
print('Precisión del modelo:', precision)
