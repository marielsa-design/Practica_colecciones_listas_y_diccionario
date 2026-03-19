# 10. Dado un diccionario, invertir las claves por los valores.

dic = {"a": 1, "b": 2, "c": 3}

def invertir(dic):
    nuevo = {}
    for k, v in dic.items():
        nuevo[v] = k
    return nuevo
    
print(invertir(dic))