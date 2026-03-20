# 13. Dada una lista de números, crear un diccionario donde la clave sea el número y el valor sea su cuadrado.

lista = [1, 2, 3, 4]

def cuadrados(lista):
    dic = {}
    for n in lista:
        dic[n] = n**2
    return dic
    
print(cuadrados(lista))