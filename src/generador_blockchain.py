import hashlib
import json
import time


class NodoBloque:
    def __init__(self, contenido, hash_anterior=''):
        self.marca_tiempo = time.time()
        self.contenido = contenido
        self.hash_anterior = hash_anterior
        self.hash_actual = self.generar_hash()

    def generar_hash(self):
        paquete = {
            'marca_tiempo': self.marca_tiempo,
            'contenido': self.contenido,
            'hash_anterior': self.hash_anterior
        }

        cadena = json.dumps(paquete, sort_keys=True).encode()
        return hashlib.sha256(cadena).hexdigest()


class CadenaBloques:
    def __init__(self):
        self.bloques = [self._bloque_inicial()]

    def _bloque_inicial(self):
        return NodoBloque('Bloque Inicial', '0')

    def ultimo_bloque(self):
        return self.bloques[-1]

    def insertar_bloque(self, contenido):
        hash_prev = self.ultimo_bloque().hash_actual
        bloque_nuevo = NodoBloque(contenido, hash_prev)
        self.bloques.append(bloque_nuevo)

    def validar_cadena(self):
        for indice in range(1, len(self.bloques)):
            actual = self.bloques[indice]
            anterior = self.bloques[indice - 1]

            if actual.hash_actual != actual.generar_hash():
                return False

            if actual.hash_anterior != anterior.hash_actual:
                return False

        return True

            if current.previous_hash != previous.hash:
                return False

        return True
