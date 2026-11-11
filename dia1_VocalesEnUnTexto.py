#Cuenta las vocales de un texto.
texto=input("Ingrese un texto: ")
vocales='aeiou'
contador=0
for letra in texto:
    if letra in vocales:
        contador+=1
print(f"El texto '{texto}' tiene {contador} vocales.")