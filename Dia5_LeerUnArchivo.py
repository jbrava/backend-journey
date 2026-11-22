#Ejercicio 13: leer un archivo de texto y contar líneas y palabras. 
#Pista: busca with open(...) as archivo: y piensa qué debería pasar si el archivo no existe.

def contar_lineas_palabras(nombre_archivo):
    with open(nombre_archivo, encoding="utf-8") as archivo:
        contenido = archivo.read()
        if not contenido:
            return None,None
        palabras = len(contenido.split())
        lineas = len(contenido.splitlines())
    return lineas, palabras

lineas,palabras=contar_lineas_palabras("workfile.txt")

if palabras is not None:
    print(f'Cantidad de lineas: {lineas} , Cantidad de palabras: {palabras}')
else:
    print('El archivo esta vacio')