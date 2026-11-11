#Quita duplicados de una lista conservando el orden. 
def eliminar_duplicados (lista):
    limpieza=[]
    
    for elemento in lista:
        if elemento not in limpieza:
            limpieza.append(elemento)
    return limpieza

lista_editada=eliminar_duplicados([])

print(f'Se eliminaron los duplicados, la lista quedó así: {lista_editada}')
