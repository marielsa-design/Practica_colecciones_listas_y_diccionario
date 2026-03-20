# 14. Agrupar una lista de palabras en un diccionario según su primera letra.

lista = ["hola", "el", "mundo", "elefante"]

def agrupar(lista):
    dic = {}
    for palabra in lista:
        letra = palabra[0]
        if letra in dic:
            dic[letra].append(palabra)
        else:
            dic[letra] = [palabra]
    return dic

print(agrupar(lista))