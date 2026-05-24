from cryptography.fernet import Fernet

# Crear clave y objeto de cifrado
clave_segura = Fernet.generate_key()
motor_cifrado = Fernet(clave_segura)

def codificar_texto(texto_plano):
    texto_bytes = texto_plano.encode()
    texto_cifrado = motor_cifrado.encrypt(texto_bytes)
    return texto_cifrado

def descodificar_texto(texto_cifrado):
    texto_descifrado = motor_cifrado.decrypt(texto_cifrado)
    return texto_descifrado.decode()

