#Dada una lista de alumnos con calificación, filtra los aprobados y calcula su promedio.
"""
def students(n):
    result = {}
    for _ in range(n):
        roll_no = int(input("Roll No: "))
        std_name = input("Student Name: ")
        marks = int(input("Marks: "))
        result[roll_no] = [std_name, marks]
    return result

n = int(input("Enter No of Students:"))
x=students(n)
print(x)
"""

def promedio_aprobados(alumnos):
    aprobados=[]
    suma=0
    nota_minima=6
    
    for alumno in alumnos:
        if alumno["calificacion"] >= nota_minima:
            aprobados.append(alumno)
            suma=suma+alumno["calificacion"]
    
    if not aprobados:
        return aprobados, None

    promedio = suma / len(aprobados)
    return aprobados, promedio    

alumnos = [
    {"nombre": "Talia", "calificacion": 9},
    {"nombre": "Kegan", "calificacion": 7},
    {"nombre": "Josh", "calificacion": 5},
    {"nombre": "Rider", "calificacion": 6}
]

aprobados,promedio=promedio_aprobados(alumnos)

if promedio is not None:
    nombres = [alumno["nombre"] for alumno in aprobados]
    print(f"Aprobados: {nombres}. Promedio: {promedio:.2f}")
else:
    print("Nadie aprobó.")

