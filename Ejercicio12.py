# 12. Crear una lista de diccionarios que representen productos (nombre, precio, cantidad) y calcular el valor total del inventario.


def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
        return

inventario = [
    {"nombre": "manzana", "precio": 2500, "cantidad": 100},
    {"nombre": "pera", "precio": 1500, "cantidad": 250},
    {"nombre": "banana", "precio": 1200, "cantidad": 150},
    {"nombre": "uva", "precio": 3000, "cantidad": 200}
]

print("menu")
print("1. Buscar producto")
print("2. Salir")
opcion = input("Selecciona una opcion: \n")

if opcion == "1":
    nombre_producto = input("Ingrese el nombre del producto: ")
    resultado = buscar_producto(nombre_producto)

if resultado:
    print(f"Producto encontrado: {resultado["nombre"]}")
    print(f"Precio: {resultado["precio"]}")
    print(f"Cantidad: {resultado["cantidad"]}")
    print(f"Valor total en inventario: {resultado["precio"] * resultado["cantidad"]}")
    
else:
    print("Producto no encontrado.") 