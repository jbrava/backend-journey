#Reto fizzbuzz
"""
#Version 1. La primera idea que se me ocurrio
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
"""
"""
#Version 2. Tratando de realizarlo con ayuda de una funcion
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return ('FizzBuzz')
    elif n % 3 == 0:
        return ('Fizz')
    elif n % 5 == 0:
        return ('Buzz')
    else:
        return (n)

n=int(input("Introduzca un numero: "))
print(fizzbuzz(n))
"""
#Version 3. Se implemento una función y un arreglo para guardar el resultado
#Al regresarlo como result es mas facil manipularlo despues
def fizzbuzz(n):
    result=[] #arreglo para guardar los resultados
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz') #con el append se agregan al arreglo los resultados
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    return result

n=int(input("Introduzca un numero: "))
"""print(fizzbuzz(n))"""
for elemento in fizzbuzz(n):    #lee cada elemento del arreglo
    print(elemento)


