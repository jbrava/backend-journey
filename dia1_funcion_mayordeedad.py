#es_mayor_de_edad(edad), que devuelva True si la edad es 18 o más.
def es_mayor_de_edad(edad):
    return edad >= 18

#print(es_mayor_de_edad(int(input("Ingrese su edad: "))))  # True
edad = int(input("Ingrese su edad: "))
resultado = es_mayor_de_edad(edad)
#print(f"¿Es mayor de edad? {resultado}")  # True o False
if resultado:
    print("Es mayor de edad")
else:
    print("Es menor de edad")