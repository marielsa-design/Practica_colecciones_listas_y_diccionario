# 12. Crear una lista de diccionarios que representen productos (nombre, precio, cantidad) y calcular el valor total del inventario.

inventario = [
    {"nombre": "manzana", "precio": 200, "cantidad": 100},
    {"nombre": "banana", "precio": 500, "cantidad": 50},
    {"nombre": "naranja", "precio": 800, "cantidad": 30},
    {"nombre": "pera", "precio": 1200, "cantidad": 300},
    {"nombre": "uva", "precio": 200, "cantidad": 50}
]

def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
        return None
print("menu")
print("1. Buscar producto")
print("2. Salir")
opcion = input("Seleccione una opción: ")
if opcion == "1":
    nombre_producto = input("Ingrese el nombre del producto: ")
    resultado = buscar_producto(nombre_producto)
    if resultado:
        print(f"Producto encontrado:  {resultado["nombre"]}")
        print(f"Precio: {resultado["precio"]}")
        print(f"Cantidad: {resultado["cantidad"]}")
        print(f"Valor total en inventario: {resultado["precio"] * resultado["cantidad"]}")
    else:
        print("Producto no encontrado.")