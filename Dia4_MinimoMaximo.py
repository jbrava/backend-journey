#Una función que devuelva el mínimo y el máximo de una lista
"""
Devuelve los dos valores separados por una coma, y repártelos al llamarla.
No uses min() ni max(): haz el recorrido tú, con la misma idea que en estadistica.
Decide qué devuelve con la lista vacía (None, un error u otro valor) y anótalo en un comentario.
"""

#[14, 8, 1, 10, 2], [-5, -2, -9], [7] y []
def minimo_maximo (lista):
    if not lista:
        return None, None

    maximo = lista[0]
    minimo = lista[0]

    for valor in lista:
        if valor > maximo:
            maximo=valor
        if valor < minimo:
            minimo=valor
    return maximo,minimo

lista = []

maximo,minimo=minimo_maximo(lista)

if maximo is not None:
    print(f'Minimo: {minimo} , Maximo: {maximo}')
else:
    print('La lista esta vacía')