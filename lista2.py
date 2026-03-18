# 2. Dada una lista de números, contar cuántos son pares y cuántos impares.

listas_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num1 = input("Ingresar su numero mayor: ")
num2 = input("Ingresar su numero menor: ")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")