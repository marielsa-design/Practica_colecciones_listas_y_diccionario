# 15. Dada una lista de ventas (diccionarios con producto y monto), calcular el total vendido por cada producto.

ventas = [
    {"producto": "arroz", "monto": 1000},
    {"producto": "pasta", "monto": 2200},
    {"producto": "yuca", "monto": 1500},
    {"producto": "pan", "monto": 500},
    {"producto": "sal", "monto": 100}
]

def total_ventas(lista):
    dic = {}
    for v in lista:
        p = v["producto"]
        if p in dic:
            dic[p] += v["monto"]
        else:
            dic[p] = v["monto"]
    return dic

print(total_ventas(ventas))