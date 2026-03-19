# 2. Dada una lista de números, contar cuántos son pares y cuántos impares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def contar_pares_impares(lista):
    pares = 0
    impares = 0

    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares 

resultado = contar_pares_impares(lista) 
print("impares e impares: ", resultado)