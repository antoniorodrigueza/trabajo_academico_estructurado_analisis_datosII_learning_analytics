import sys
sys.path.append('/content/trabajo_academico_estructurado_analisis_datosII_learning_analytics/src')

from cifrador import codificar_texto as cifrar_texto, descodificar_texto as descifrar_texto

def comprobar_cifrado():
    
    cadena_original ='Ana'
    valor_cifrado = codificar_texto(cadena_original)
    valor_descifrado = descodificar_texto(valor_cifrado)

    assert cadena_original == valor_descifrado, \
        f"Error: '{cadena_original}' != '{valor_descifrado}'"

    print("Cifrado y descifrado correctos")


