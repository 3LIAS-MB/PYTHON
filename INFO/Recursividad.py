"""-------------------------------------------------------------------------FUNCION RECURSIVA-----------...............-------------------------------------------"""
"""Una función recursiva es una función que se llama a sí misma durante su ejecución. En otras palabras, una función recursiva resuelve un
problema dividiéndolo en subproblemas más pequeños y luego resolviendo cada subproblema utilizando la misma función."""

#La recursión implica dos componentes principales:
#EL CASO BASE:  El caso base establece una condición en la que la función deja de llamarse a sí misma y devuelve un resultado directamente."""
#El CASO RECURSIVO: es donde la función se llama a sí misma para resolver el problema de manera incremental, dividiéndolo en problemas más pequeños."""

"""Al utilizar la recursión, es importante asegurarse de que el caso base eventualmente se cumpla para evitar una llamada infinita y causar un desbordamiento de pila (STACK).
Además, cada llamada recursiva debe acercarse al caso base para garantizar la terminación de la función."""

#LLAMADA RECURSIVA DIRECTA: ignifica que una función se llama a sí misma directamente dentro de su propio cuerpo de código. En otras palabras, la función hace referencia
#explícita a su propio nombre en su implementación para invocarse a sí misma. 

def factorial_directo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_directo(n - 1)

#LLAMADA RECURSIVA INDIRECTA ocurre cuando una función se llama a sí misma a través de otra función, es decir, no se hace referencia directa al nombre de la función en
#su propia implementación. En lugar de eso, otra función o método llama a la función recursiva.

def factorial_indirecto_helper(n):
    if n == 0:
        return 1
    else:
        return n * factorial_indirecto_helper(n - 1)

def factorial_indirecto(n):
    return factorial_indirecto_helper(n)

#Pila de llamadas: proceso LIFO (Last Input First Output) "El ultimo en entrar es el primero en salir" #"Desbordamiento de pila" o "Stack Overflow"

#CUANDO SE EJECUTA EL PROGRAMA EN LA MEMORIA SE CREA UN ESPACIO QUE SE DENOMINA STACK (O PILA) Y ESTE STACK FUNCIONA COMO UNA ESTRUCTURA DE DATOS PILA (EL ULTIMO ELEMENTO
#QUE ENTRA ES EL PRIMERO QUE SALE), ¿y que cosa entra y sale de la pila? UN CUADRO, FRAME (FREIM) QUE TIENE TODOS LOS ELEMENTOS RELACIONADOS A ESA FUNCION, Y ESO EXPLICA
#PORQUE CUANDO MANDAMOS A LLAMAR UNA FUNCION Y ESTA TERMINA, REGRESAMOS A LA FUNCION PREVIA Y CONTINUAMOS CON LO QUE NOS HABIAMOS QUEDADO, CUANDO SE LLAMA ASI MISMO SE CREA UN FRAME

#EJEMPLOS

#CUENTA REGRESIVA
def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("HOLAAA")
        
    print(f"Orden de liberacion {numero}") #de esta forma se libera la memoria ram
    
#ORIGINAL
cuenta_atras(10)
#-----------------------------------------------------------
#CASO PARA CALCULAR EL FACOTORIAL DE UN NUMERO
def calcular_factorial(numero):
    if numero > 1:
        numero = numero * calcular_factorial(numero - 1)
    return numero

# def calcular_factorial(numero):
#     if numero > 1: numero *= calcular_factorial(numero - 1)
#     return numero

print(calcular_factorial(5))
#---------------------------------------------------------
#FORMA ITERATIVA (CASO DE CONTAR TODAS LAS HOJAS DE DIFERENTES LIBROS)
libros = [50, 100, 150, 70, 250]
total = 0
for libro in libros:
    total += libro

print(total)

#FORMA RECURSIVA (CASO DE CONTAR TODAS LAS HOJAS DE DIFERENTES LIBROS)
def totalPaginas(libros):
    if len(libros) == 1:
        return libros[0]
    
    return libros[0] + totalPaginas(libros[1:])

totalPaginas([50, 100, 150])
#-------------------------------------------------------------
#CASO DE FIBONACCI
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))

#DE LA FORMA ITERATIVA
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a