# 5. Dada una lista de notas, calcular el promedio y mostrar si el estudiante aprueba (>= 3.0).

lista = [3.5, 4.0, 2.8 , 3.2]

def lista_nota(lista):
    suma = 0

    for nota in lista:
       suma += nota

    promedio = suma / len(lista)

    if promedio >= 3.0:
        estado = "Aprueba"
    else:
        estado = "Reaprueba"
    return promedio, estado

resultado = lista_nota(lista) 
print("Resultado: ", resultado)