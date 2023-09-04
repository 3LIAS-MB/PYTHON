# Lista de claves numéricas
lista = [10, 20, 30, 40]
claves_lista = list(range(len(lista)))

print(claves_lista)

# Tupla de claves alfabéticas
tupla = ("a", "b", "c", "d")
claves_tupla = [tupla.index(clave) for clave in tupla]

print(claves_tupla)
"""-------------------------------------------------------------"""
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))

matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)

for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento), end=" ")
    print("]")  
print() 
"""_---------------------------------------------------------------"""
# import math

# def exponential_power_series(x, n):
#     result = 0.0
#     for i in range(n):
#         result += (x**i)/math.factorial(i)
#     return result

# #original
# x = int(input("Ingreasr x: "))
# n = int(input("Ingreasr x: "))
# print(exponential_power_series(x, n))

# print("Ingrese un numero: ")
# num = int(input(""))
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print(f"El factorial de {num} es: {fact}")