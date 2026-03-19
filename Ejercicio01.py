## Listas ##
# 1. Crear una lista de 10 números enteros e imprimir el número mayor.

lista = [7, 1, 10, 2, 4, 9, 5, 3, 6, 8] # OJO NO SE OLVIDÉ PONER LA "LISTA"

def numero_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor # Retonar es decir se delvuelve

resultado = numero_mayor(lista) # OJO NO SE OLVIDÉ IMPRIMIR EL "PRINT" Y "RESULTADO"
print("El numero mayor es: ", resultado)
