from cifrador import codificar_texto, descodificar_texto

def comprobar_cifrado(cadena_original):
    
    valor_cifrado = codificar_texto(cadena_original)
    valor_descifrado = descodificar_texto(valor_cifrado)

    assert cadena_original == valor_descifrado, \
        f"Error: '{cadena_original}' != '{valor_descifrado}'"

    print("Cifrado y descifrado correctos")


