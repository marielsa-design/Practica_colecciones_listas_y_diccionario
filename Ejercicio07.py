# 7. Dado un diccionario de estudiantes y sus notas, calcular el promedio general

estudiantes = {
    "Carlos": 85,
    "Maria": 95,
    "Andrés": 58,
    "Jorge": 84,
    "Ana": 95,
}

def promedio_estudiantes(dic):
    suma = 0
    
    for nota in dic.values():
        suma += nota

    promedio = suma / len(dic)
    return promedio

resultado = promedio_estudiantes(estudiantes)
print(resultado)