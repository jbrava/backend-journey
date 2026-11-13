#Cuenta la frecuencia de cada palabra de un texto.
#Version 1. El primer intento
"""
texto=('')
resultado=texto.lower().strip().split()
frecuencia={}

for palabra in resultado:
    if palabra not in frecuencia:
        frecuencia[palabra] = 1
    else:
        x = frecuencia.get(palabra)
        frecuencia.update({palabra: x+1}) 

print(resultado)
print(frecuencia)
"""
#Version 2. Se compacto
def contar_palabras(texto):
    frecuencia = {}
    for palabra in texto.lower().strip('?¡!¿.').split():
        frecuencia[palabra] = frecuencia.get(palabra,0) + 1
    return frecuencia

texto=input("Introduce el texto: ")
print(f'Frecuencia de las palabras en el texto: {contar_palabras(texto)}')