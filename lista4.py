# 4. Eliminar los elementos duplicados de una lista y mostrar la nueva lista.

lista = ["Perro", "Gato", "Conejo", "Loro", "Pez"]
eliminar = []

for i in range(len(lista)):
    eliminar.remove("Loro")

print(lista)