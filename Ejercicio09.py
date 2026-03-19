# 9. Crear un diccionario que almacene el nombre de 5 personas y su edad, luego mostrar las personas mayores de 18 años.

presonas = {"Carlos": 15, "Maria": 17, "Andrea": 19,"Luis": 18, "Fabiana": 20}

def mayores(dic):
    lista = []
    for nombre, edad in dic.items():
        if edad >= 18:
            lista.append(nombre)
    return lista

print(mayores(presonas))