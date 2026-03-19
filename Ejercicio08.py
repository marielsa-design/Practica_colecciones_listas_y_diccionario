# 8. Contar cuántas veces aparece cada palabra en una frase usando un diccionario

frase = "Hola el mundo mundo Hola el"

def contar(frase):
    dic = {}
    for p in frase.split():
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    return dic

print(contar(frase))