# 6. Crear un diccionario con nombres de 5 productos y sus precios, luego mostrar el producto más caro.

producto = {
    "Arroz": 2000,
    "Azucar": 1200,
    "Leche": 1200,
    "Cafe": 2400,
    "Chocolate": 3000,
}

def producto_mas_caro(dic):
    mayor = 0
    nombre = ""

    for producto, precio in dic.items():
        if precio > mayor:
            mayor = precio
            nombre = producto
    return nombre, mayor

resultado = producto_mas_caro(producto) 
print("El producto es más caro: ", resultado)