#Validar una contraseña (mínimo de longitud, una mayúscula y un número) 
# y devolver True o False. 
# Pista: mira los métodos .isupper() y .isdigit(), y la función any(...) 

def validar_password(password, longitud_minima=8):
    problemas = []

    if len(password) < longitud_minima:
        problemas.append("Debe tener mínimo 8 caracteres")

    if not any(char.isdigit() for char in password):
        problemas.append("Debe conter al menos un número")

    if not any(char.isupper() for char in password):
        problemas.append("Debe conter al menos una mayúscula")

    if " " in password:
        problemas.append("No puede contener espacios")

    return problemas


problemas = validar_password(input('Introduzca la contraseña a validar: '))

if problemas:
    print("Contraseña invalida: " + ", ".join(problemas))
else:
    print("Contraseña válida")



