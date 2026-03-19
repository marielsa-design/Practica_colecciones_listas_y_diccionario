# 3. Invertir el orden de una lista sin usar funciones propias del lenguaje.

lista = [1, 2, 3, 4, 5,]
invertida = []

for i in range(len(lista)-1, -1, -1):
    invertida.append(lista[i])

print(invertida)