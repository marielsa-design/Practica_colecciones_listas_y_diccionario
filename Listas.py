## Listas ##
# 1. Crear una lista de 10 números enteros e imprimir el número mayor.

def numero_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
        return mayor

# 2. Dada una lista de números, contar cuántos son pares y cuántos impares.}

def contar_pares_impares(lista):
    pares = 0
    impares = 0

    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        return pares, impares

# 3. Invertir el orden de una lista sin usar funciones propias del lenguaje.

def invertir_lista(lista):
    invertida = []

    i = 0
    for _ in lista:
        i -= 1
    
    while i > 0:
        invertida.append(lista[i - 1])
        i -= 1
        return invertida

# 4. Eliminar los elementos duplicados de una lista y mostrar la nueva lista.

def eliminar_duplicados(lista):
    nueva = []

    for num in lista:
        if num not in nueva:
            nueva.append(num)
        return nueva

# 5. Dada una lista de notas, calcular el promedio y mostrar si el estudiante aprueba (>= 3.0).

def promedio_notas(lista):
    suma = 0
    contador = 0

    for nota in lista:
        suma += nota
        contador += 1

    promedio = suma / contador

    if promedio >= 3.0:
        estado = "Aprueba"
    else:
        estado = "No aprueba"
        return promedio, estado
    
numeros = [5, 8, 12, 3, 9, 20, 7, 15, 2, 10]
print("1. Número mayor:", numero_mayor(numeros))

pares, impares = contar_pares_impares(numeros)
print("2. Pares:", pares, "impares", impares)

print("3. Lista invertida:", invertir_lista(numeros))

lista_dup = [1,1,2,2,3,3,4,4,5,5]
print("4. Sin duplicados:", eliminar_duplicados(lista_dup))

notas= [2.8, 3.2, 3.5, 4.0,]
promedio, estado = promedio_notas(notas)
print("5. Promedio:", promedio)
print("Estado:", estado)
