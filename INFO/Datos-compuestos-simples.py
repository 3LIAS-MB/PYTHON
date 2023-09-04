"""---------------------------------------DATOS SIMPLES--------------------------------------"""
"""--------------------------------------TIPOS DE DATOS--------------------------------------"""

"""1) TEXTO -> string: cadena de texto """
#Si escribimos texto en una linea usamos un par de comillas ("hello world") y si ocupamos más de
#una usamos triple comillas ("""hello world""")

"""2) NUMERO -> int: los numeros enteros; float: numeros flotantes, con coma"""
"""3) VALORES BOOLEANOS -> False or True: ambos van con mayuscula inicial"""

"""-------------------------------VARIABLES----------------------------------------------"""
nombre = "Elias" #--> en "nombre" estoy declarando la variable y en "Elias" la estoy definiendo
print(nombre)
#
numero = 10
numero += 5 #Esta es otra forma de sumar, vez de poner "numero = 10 + 5"
print(numero) 
"""-------------------------------#CONCATENAR----------------------------------------------"""
nombre = "Elias"
bienvenida = "Hola, " + nombre + ", ¿como estas?" #es una forma pero si cambiamos "Elias" por un número sale error porque es un tipo numerico
print(bienvenida)
"""------------------------------#USANDO F STRING---------------------------------------------"""
nombre = "Elias"
bienvenida = f"Hola {nombre} ¿como estas?"
print(bienvenida)
"""-----------------------#OPERADORES DE PERTENENCIA (IN/NOT IN)--------------------------"""
nombre = "Elias"
bienvenida = f"Hola {nombre} ¿como estas?"
print("Elias" not in bienvenida)
"""-------------------------------#DEFINIR VARIABLE-----------------------------------------"""
#Definiendo una variable con camelCase
nombreCompletoPeroConMayusculaInicial = 'Elias'
#Definiendo una variable con snake_case
nombre_completo_pero_con_mayuscula_inicial = 'Elias' #recomendado
#-------------------------------------------------------
"""------------------------------------DATOS COMPUESTOS---------------------------------"""

"""-------------------------------------LISTAS--------------------------------------------------------------------"""
"""LISTA: ES UN TIPO DE MATRIZ, CONJUNTO DE DATOS QUE SE PUEDEN MODIFICAR: Podemos borrar elementos, cambiar, añadir, etc"""
#En python se cuenta del 0 hasta el ultimo elemento
#EL INDICE "-1" EN LAS LISTAS INDICA EL ULTIIMO ELEMENTO QUE ESTA TIENE
#IMPRIMIMOS SUBLLITAS SEPARANDO EL NUMERO POR DOS PUNTOS "print(lista[1:2])"
#si no le indicamos el inicio comienza desde 0
#si no le indicamos final finaliza en el ultimo elemento

lista = ["Elias", "Braulio", True, 1.60] #"Elias" es 0; "Braulio" es 1; "True" es 2 y "1".60" es 3
print(lista[1:2]) 

"""1. Ordenadas:
Las listas en Python son colecciones ordenadas de elementos. Los elementos en una lista mantienen el orden en el que se agregaron
y se acceden mediante índices."""
lista = [1, 2, 3, 4, 5]
print(lista)  # Salida: [1, 2, 3, 4, 5]

print(lista[0])  # Salida: 1

"""2. Pueden contener elementos duplicados:
A diferencia de los conjuntos, las listas pueden contener elementos duplicados."""
lista = [1, 2, 2, 3, 3, 4, 5]
print(lista)  # Salida: [1, 2, 2, 3, 3, 4, 5]

"""3. Mutabilidad:
Las listas son mutables, lo que significa que se pueden modificar agregando, eliminando o modificando elementos."""
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Salida: [1, 2, 3, 4]

lista.remove(2)
print(lista)  # Salida: [1, 3, 4]

lista[0] = 5
print(lista)  # Salida: [5, 3, 4] | CAMBIAR EL VALOR DE UNA LISTA

lista.pop(2)
print(lista) # Salida [1, 2]

del lista[1]
print(lista) # Salida [1, 3]

"""4.Pueden contener elementos de diferentes tipos:
Las listas en Python pueden contener elementos de diferentes tipos de datos, como enteros, cadenas, flotantes, booleanos,
e incluso otras listas u objetos."""
lista = [1, "Hola", 3.14, True]
print(lista)  # Salida: [1, 'Hola', 3.14, True]

lista_anidada = [[1, 2, 3], [4, 5, 6]]
print(lista_anidada)  # Salida: [[1, 2, 3], [4, 5, 6]]

"""Estas son algunas de las características clave de las listas en Python. Las listas son una estructura de datos versátil
y ampliamente utilizada que permite almacenar y manipular colecciones de elementos de manera flexible."""
"""-------------------------------------TUPLAS--------------------------------------------------------------------"""

"""*****TUPLAS: CONJUNTO DE DATOS QUE NO SE PUEDEN MODIFICAR, QUEDAN TAL CUAL HASTA EL FINAL DEL PROGRAMA*********"""

"""1. nmutabilidad: Las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas. No es posible agregar, eliminar o
modificar elementos individuales dentro de una tupla. Sin embargo, es posible crear nuevas tuplas a partir de tuplas existentes o combinar
tuplas para formar nuevas."""

#Creación de una tupla
tupla = (1, 2, 3)
print(tupla)

tupla = 1, 2, 3, 4, 5
print(tupla)

tupla = tuple([1, 2, 3, 4, 5])
print(tupla)

#Intento de modificar la tupla (generará un error)
tupla[0] = 4

"""2. Orden: Las tuplas mantienen el orden de los elementos. Los elementos se almacenan en la tupla en el orden en que se agregaron y se puede
acceder a ellos por su posición mediante indexación.""" 
# Acceso a elementos de una tupla mediante índices
tupla = (10, 20, 30, 40, 50)
print(tupla[0])  # Salida: 10
print(tupla[3])  # Salida: 40

# Recorrido de una tupla utilizando un bucle for
for elemento in tupla:
    print(elemento)
"""3. Indexación: Al igual que las listas, las tuplas permiten acceder a sus elementos utilizando índices. Los índices se utilizan para
referirse a elementos individuales dentro de la tupla. La indexación comienza desde 0 para el primer elemento y se extiende hasta n-1 para
el último elemento, donde n es la longitud de la tupla."""
# Acceso a elementos de una tupla mediante índices
tupla = (10, 20, 30, 40, 50)
print(tupla[0])  # Salida: 10
print(tupla[3])  # Salida: 40

# Recorrido de una tupla utilizando un bucle for
for elemento in tupla:
    print(elemento)
"""4. Heterogeneidad: Las tuplas pueden contener elementos de diferentes tipos de datos. Puedes combinar diferentes tipos de elementos en una
tupla, como enteros, cadenas, booleanos, etc."""
#Tupla con elementos de diferentes tipos
tupla = (10, "Hola", True)
print(tupla)

"""5. Los paréntesis no son estrictamente necesarios para definir una tupla; incluso se pueden crear sin paréntesis, utilizando solo comas
para separar los elementos."""
# Creación de una tupla sin paréntesis
tupla = 1, 2, 3
print(tupla)

"""Recuerda que, a diferencia de las listas, las tuplas no admiten operaciones de modificación directa, como agregar, eliminar o cambiar
elementos. Por lo tanto, se utilizan principalmente en situaciones donde se necesita una estructura de datos inmutable y con un conjunto fijo
de elementos. Las tuplas ocupan menos espacio en memoria que las listas, beneficioso si se necesita algo inmutable y eficiente en termino de memoria"""
#POR EJEMPLO, SI QUISIERAMOS BORRAR
tupla.pop(1) #-> No se puede
print(tupla)
"""------------------------------------CONJUNTOS----------------------------------------"""
#CONJUNTO (SET): NO tienen un orden fijo, NO puede haber datos duplicados y NO se puede acceder por el indice (ya que no tienen orden)
#SETS: son colleciones desordenadas de objetos unicos, pueden ser listas, tuplas, otros diccionarios
#Los conjuntos se utilizan principalmente para verificar la existencia de elementos y realizar operaciones matemáticas de conjuntos,
#como unión, intersección y diferencia.

conjunto = {'manzana', 'platano', 'pera', 'manzana', 'naranja', 'pera'}
#print(conjunto[3]) -> no puede acceder al elemento // este seria el indice
print(conjunto)

"""1. Elementos únicos:
Los conjuntos no pueden contener elementos duplicados. Si intentas agregar un elemento duplicado a un conjunto, este se ignorará."""
conjunto = {1, 2, 3, 4, 5}
print(conjunto)  # Salida: {1, 2, 3, 4, 5}

conjunto = {1, 2, 2, 3, 3, 4, 5}
print(conjunto)  # Salida: {1, 2, 3, 4, 5} (se ignoran los elementos duplicados)

"""2. No tienen un orden definido:
Los elementos de un conjunto no están en un orden específico y no se acceden mediante índices.
Al imprimir un conjunto, el orden de los elementos puede variar."""
conjunto = {3, 1, 2}
print(conjunto)  # Salida: {1, 2, 3}

"""3. Mutabilidad:
Los conjuntos son mutables, lo que significa que se pueden modificar agregando o eliminando elementos."""
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Salida: {1, 2, 3, 4}

conjunto.remove(2)
print(conjunto)  # Salida: {1, 3, 4}

"""4. Operaciones matemáticas de conjuntos:
Los conjuntos en Python admiten operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica."""
A = {1, 2, 3}
B = {3, 4, 5}

union = A | B
print(union)  # Salida: {1, 2, 3, 4, 5}

interseccion = A & B
print(interseccion)  # Salida: {3}

diferencia = A - B
print(diferencia)  # Salida: {1, 2}

diferencia_simetrica = A ^ B
print(diferencia_simetrica)  # Salida: {1, 2, 4, 5}
"""------------------------------------DICCIONARIOS----------------------------------------"""

"""1. Asociación clave-valor:
Los diccionarios en Python son colecciones de elementos que se almacenan como pares clave-valor. Cada elemento del diccionario tiene una
clave única que se utiliza para acceder a su valor correspondiente."""
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(diccionario)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}

print(diccionario["nombre"])  # Salida: Juan

"""2. No ordenados:
A diferencia de las listas y las tuplas, los diccionarios no tienen un orden específico.
Los elementos de un diccionario se almacenan de forma desordenada y no se acceden mediante índices."""

"""3. Mutabilidad:
Los diccionarios son mutables, lo que significa que se pueden modificar agregando, eliminando o modificando elementos."""

diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
#AGREGANDO
diccionario["profesion"] = "Ingeniero"
print(diccionario)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}
#ELIMINANDO
del diccionario["edad"]
print(diccionario)  # Salida: {'nombre': 'Juan', 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

"""4. Claves únicas:
Las claves en un diccionario son únicas, lo que significa que no puede haber claves duplicadas en un mismo diccionario.
Si se intenta agregar un valor con una clave que ya existe, se reemplazará el valor existente."""

diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

diccionario["nombre"] = "Pedro"
print(diccionario)  # Salida: {'nombre': 'Pedro', 'edad': 25, 'ciudad': 'Madrid'}

#en un diccionario se accede al valor del elemento por su clave, NO ES EL INDICE!
equipo = {10:"Paulo Dybala", 11:"Douglas Costa", 7:"Cristiano Ronaldo",17:"Mario Mandzukic"} #clave tipo entero
print(equipo[6]) 

#OTRO EJEMPLO #clave y el valor un diccionario y dos listas
diccionario = {"Alejandro": {"edad":22, "estatura":1.73}, "José":[21, 1.75], "Maria":[22, 1.67]}
print(diccionario)
"""-----------------------------------random.choice() and random.randint()----------------------------------------------------------------"""
"""random.choice() se utiliza para elegir aleatoriamente un elemento de una secuencia, como una lista o una tupla.
Recibe como argumento una secuencia y devuelve un elemento aleatorio de esa secuencia."""

"""random.randint() se utiliza para generar un número entero aleatorio dentro de un rango especificado. Recibe dos argumentos: el valor más bajo
del rango y el valor más alto del rango, y devuelve un número entero aleatorio dentro de ese rango,incluyendo ambos extremos."""