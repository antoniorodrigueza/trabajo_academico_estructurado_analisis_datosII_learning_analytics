from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Preparación de variables
caracteristicas = df[['participation']]
objetivo = (df['grade'] < 6).astype(int)

# División del dataset
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    caracteristicas,
    objetivo,
    test_size=0.2,
    random_state=42
)

# Modelo
clasificador = LogisticRegression()
clasificador.fit(x_entrenamiento, y_entrenamiento)

# Predicciones
etiquetas_predichas = clasificador.predict(x_prueba)

# Métrica
precision = accuracy_score(y_prueba, etiquetas_predichas)
print('Precisión del modelo:', precision)
