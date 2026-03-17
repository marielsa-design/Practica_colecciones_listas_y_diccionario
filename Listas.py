## Listas ##
# 1. Crear una lista de 10 números enteros e imprimir el número mayor.
# 2. Dada una lista de números, contar cuántos son pares y cuántos impares.
# 3. Invertir el orden de una lista sin usar funciones propias del lenguaje.
# 4. Eliminar los elementos duplicados de una lista y mostrar la nueva lista.
# 5. Dada una lista de notas, calcular el promedio y mostrar si el estudiante aprueba (>= 3.0).

num_enteros = [{1, 2, 3, 4, 5, 6, 7, 8, 9, 10,}]
pares = [{2, 4, 6, 8, 10,}]
impares = [{1, 3, 5, 7, 9}]

opcion = 1
numero = []
pares = 0
impares = 0

# enteros
# pares
# impar

orden_lista = [
    {"enteros": 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    {"pares": 2, 4, 6, 8, 10}
    {"impar": 1, 3, 5, 7, 9}
]

while opcion != 0:

    for i, num_enteros in enumerate(numero, start=1):
        print(f"{i} {num_enteros[ "numeros"]}")

    opcion = int(input("escoja un numero o ingresar 0 para salir"))

    if opcion == 0:
        break

    pares_escogido = num_enteros[opcion-1]
    numero_pare = pares_escogido["numero"]

    existe = False

    for heroe in equipo:
        if heroe["numero"] == numero_pare:
            existe = True
            break

    if existe:
        print("el heroes ya está en la lista.")
    else:
        pares.append(num_enteros[opcion-1])
        print(f"{num_enteros} agregado al equipo")

# 5. Dada una lista de notas, calcular el promedio y mostrar si el estudiante aprueba (>= 3.0).