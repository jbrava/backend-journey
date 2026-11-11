# Palíndromo opcion 1
"""
texto=input("Ingrese un texto: ")
texto_invertido=texto[::-1]
if texto.replace(" ", "").lower() == texto_invertido.replace(" ", "").lower():
    print("Es un palíndromo")  
else:
    print("No es un palíndromo")

"""
#Opcion 2 en una función
def es_palindromo(texto):
    #texto_invertido = texto[::-1]
    texto_limpio = texto.replace(" ", "").lower()
    #return texto.replace(" ", "").lower() == texto_invertido.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

print(es_palindromo(input("Ingrese un texto: ")))  # True


# Opcion 3 Con reversed() y join
#invertida = "".join(reversed(texto))
