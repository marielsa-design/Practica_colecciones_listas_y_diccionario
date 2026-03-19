# 11. Dada una lista de diccionarios con datos de estudiantes (nombre y nota), mostrar el estudiante con mejor nota.

estudiantes = [
    {"Nombre": "Carlos", "nota": 85},
    {"Nombre": "Mario", "nota": 45},
    {"Nombre": "Andrea", "nota": 62},
    {"Nombre": "Daniel", "nota": 80},
    {"Nombre": "Gabriela", "nota": 95},
    {"Nombre": "Mariano", "nota": 35},
    {"Nombre": "Maya", "nota": 75}
]

def mejor(lista):
    m = lista[0]
    for e in lista:
        if e["nota"] > m["nota"]:
            m = e
        return m
    
print(mejor(estudiantes))