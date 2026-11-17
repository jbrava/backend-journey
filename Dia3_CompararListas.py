#Escribe una función que reciba dos listas 
#y devuelva los elementos que aparecen en ambas, usando conjuntos (sets).
def elementos_comunes(lista_a, lista_b):
    return sorted(set(lista_a) & set(lista_b))

lista1 = []
lista2 = [3, 4]

print(elementos_comunes(lista1,lista2))

"""
print(conjunto1)            # unique letters in conjunto1
print(conjunto1-conjunto2)  # letters in conjunto1 but not in conjunto2
print(conjunto1|conjunto2)  # letters in conjunto1 or conjunto2 or both
print(conjunto1&conjunto2)  # letters in both conjunto1 and conjunto2
print(conjunto1^conjunto2)  # letters in conjunto1 or conjunto2 not both
"""