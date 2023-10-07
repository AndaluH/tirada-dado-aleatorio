### App de una tirada aleatoria de cualquier tipo de dado 

import random

def numero_aleatorio():
    
    dado = int(input("¿que tipo de dado quieres usar? "))
    
    return random.randint(1, dado)

# Ejemplo de uso:
aleatorio = numero_aleatorio()
print(aleatorio)
