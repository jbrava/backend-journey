#Convertir temperaturas entre °C y °F, validando la entrada. Las fórmulas:
#°C a °F: multiplica por 9/5 y suma 32.
#°F a °C: resta 32 y multiplica por 5/9.

def convertir_temperatura(temperatura,opcion):
    if opcion==1:
        conversion=(temperatura * (9 / 5)) + 32
    elif opcion==2:
        conversion=(temperatura-32) *(5/9)  
    else:
        return None
    return conversion

temperatura=float(input('Introduce la temperatura a convertir: '))
opcion=int(input('Para convertir de Celsius a Fahrenheit presione 1, de Fahrenheit a Celsius presione 2: '))

conversion=convertir_temperatura(temperatura,opcion)

if conversion is not None: 
    if opcion==1:
        print(f'{temperatura} °C es igual a {conversion:.1f} °F')
    elif opcion==2:
        print(f'{temperatura} °F es igual a {conversion:.1f} °C')
else:
    print('Opción inválida')