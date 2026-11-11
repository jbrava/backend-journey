#Suma, promedio, máximo y mínimo de una lista, sin usar sum, max ni min.
"""
#Opcion 1 esto es lo primero que se me ocurrio
lista=[14,8,1,10,2]
suma=0
total=0
maximo=lista[0]
minimo=lista[0]

for numero in lista:
    total = total + 1
    suma = suma + numero
    if maximo < numero : maximo = numero
    if minimo > numero : minimo = numero

promedio=suma/total
print(f'La lista contiene {total} numeros, la suma de esos numero es {suma} ,el promedio es {promedio} , el maximo es {maximo} y el minimo es {minimo}')
"""

#Opcion 2, aqui se mejoro y se transformo en una función
def estadistica(lista):
    if not lista:
        return None, None, None, None
    
    suma=0
    total=0
    maximo=lista[0]
    minimo=lista[0]

    for numero in lista:
        total = total + 1
        suma = suma + numero
        if maximo < numero: 
            maximo = numero
        if minimo > numero: 
            minimo = numero    
        
    promedio=suma/total

    return suma,promedio,maximo,minimo

suma,promedio,maximo,minimo=estadistica([14, 8, 1, 10, 2])
if suma is not None:
    print(f'La suma de estos números es {suma} ,su promedio es {promedio} , el máximo es {maximo} y el mínimo es {minimo}.')   
else:
    print("La lista está vacía")