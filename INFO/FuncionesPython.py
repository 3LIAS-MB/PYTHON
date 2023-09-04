"""---------------------------------------------FUNCION LAMBDA-----------------------------------------------------------"""
"""La función lambda es una forma de crear funciones anónimas y puede usarse en diferentes contextos y con diferentes tipos de datos,
incluyendo listas, diccionarios, tuplas, números, cadenas, etc. Ejemplo:"""

"""La función lambda te permite crear funciones pequeñas y expresivas en línea, sin necesidad de definir una función con un nombre específico.
Puedes usarla en diferentes contextos donde necesites una función rápida y concisa."""

#1. Con listas
lista = [1, 2, 3, 4, 5]
resultado = list(filter(lambda x: x > 3, lista))

#2. Con cadenas
cadena = "Hola, mundo!"
resultado = "".join(map(lambda x: x.upper(), cadena))

#3. Con numeros
numero = 5
doble = (lambda x: x * 2)(numero)



""""key=lambda" se utiliza en funciones de ordenamiento y transformación para especificar una función de clave personalizada.
La función lambda se utiliza dentro de la cláusula "key" para proporcionar la lógica de la clave personalizada."""
    
frutas = ["manzana", "banana", "cereza", "kiwi", "naranja"]

# Ordenar la lista de frutas por la longitud de cada elemento
frutas_ordenadas = sorted(frutas, key=lambda x: len(x))

print(frutas_ordenadas) #['kiwi', 'banana', 'cereza', 'manzana', 'naranja'].

"""-------------------------------------------------------------any()-----------------------------------------------------------------------
La función any() es una función incorporada en Python que se utiliza para verificar si al menos un elemento de un iterable es verdadero.
A continuación, te explico cómo funciona: any(iterable) recibe un iterable como argumento, como una lista, tupla, conjunto o generador.
Itera sobre los elementos del iterable y evalúa cada uno de ellos en un contexto booleano. Devuelve True si al menos uno de los elementos
es evaluado como verdadero (distinto de cero, vacío o False). Devuelve False si todos los elementos son evaluados como falsos.

Aquí hay un ejemplo para ilustrar su uso:"""

valores = [False, 0, '', None, True, 42, 'Hola']

resultado = any(valores)
print(resultado)  # True
