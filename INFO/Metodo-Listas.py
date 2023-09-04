 
#Creando lista con list()
lista = list(["hola", "dalto", 34, 56, 23, True])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Para saber cuantas veces se repite un elemento dentro de la lista
lista = [1, "dos", 3]
print(lista.count(3))

#Busca elementos repetidos por su valor. Si el 5 está dos veces imprime 2
lista.count(5)
print(lista)

#Identificador unico
print(id(lista))
"""------------------------------------------------COPIANDO---------------------------------------------------------------------------------"""
"""1. Usar el método copy(): Puedes utilizar el método copy() para crear una copia superficial de la lista. La copia contendrá los mismos
elementos pero será un objeto diferente en memoria."""

#Crear y copiar una lista ya creada con distinto identificador
lista2 = lista.copy()
print(lista)

"""2. Usar la función list(): También puedes utilizar la función list() para crear una copia superficial de la lista."""
lista_original = [1, 2, 3]
lista_copia = list(lista_original)

"""3. Rebanado (slicing): Puedes utilizar el operador de rebanado para copiar una lista completa."""
lista_original = [1, 2, 3]
lista_copia = lista_original[:]

"""Es importante tener en cuenta que estas técnicas realizan una copia superficial, lo que significa que si la lista contiene objetos mutables
(como listas anidadas u otros objetos modificables), los cambios realizados en esos objetos se reflejarán en ambas listas.
Si necesitas una copia profunda que también copie los objetos internos, puedes usar el módulo copy de Python,
específicamente la función deepcopy()."""

import copy

lista_original = [1, 2, [3, 4]]
lista_copia = copy.deepcopy(lista_original)
"""Esto creará una copia profunda de la lista, asegurándose de que los objetos internos también se copien en lugar de compartir referencias."""

"""-------------------------------------------------AGREGANDO-----------------------------------------------------------------------"""
"""1. Usando el método append(): Este método agrega un elemento al final de la lista.  """
lista = list(["hola", "dalto", 34, 56, 23, True])
anadir = [6, 7, 8] #tambien se puede añadir cadena de texto
lista.append(anadir) #añade la lista como sublista
print(lista)

"""2. Usando la concatenación de listas: Puedes concatenar una lista existente con otra lista que contenga solo el elemento que deseas agregar."""
#lista = lista + [elemento]

"""3. Usando el método insert(): Este método te permite insertar un elemento en una posición específica de la lista."""
#lista.insert(posicion, elemento)

lista = list(["hola", "dalto", 34, 56, 23, True])
lista.insert(2,"HOLA") #en este caso reemplaza a 34 y 34 se mueve 1 lugar +
#Insertar "Hola" en el indice 2

"""4. Usando el método extend(): Si tienes una lista adicional y quieres agregar todos sus elementos a la lista original,
puedes usar el método extend()."""
#AGREGANDO UNA LISTA A OTRA LISTA
lista = [1, 2, 3]
nuevos_elementos = [4, 5, 6]

lista.extend(nuevos_elementos)
print(lista)  # Salida: [1, 2, 3, 4, 5, 6]

#AGREGANDO UNA TUPLA A UNA LISTA (LA TUPLA AHORA ES PARTE DE LA LISTA)
lista = [1, 2, 3]
nuevos_elementos = (4, 5, 6)

lista.extend(nuevos_elementos)
print(lista)  # Salida: [1, 2, 3, 4, 5, 6]

#AGREGANDO UNA TUPLA (QUE TIENE UN RANGE) A UNA LISTA
lista = [1, 2, 3]
nuevos_elementos = range(4, 7)

lista.extend(nuevos_elementos)
print(lista)  # Salida: [1, 2, 3, 4, 5, 6]

#AGREGANDO UNA CADENA A UNA LISTA
lista = [1, 2, 3]
cadena = "abc"
lista.extend(cadena)
print(lista) # Salida [1, 2, 3, 'a', 'b', 'c']

"""La cadena "abc" se agrega a la lista como elementos individuales, de modo que cada carácter ('a', 'b' y 'c')
se convierte en un elemento de la lista resultante."""

"""-------------------------------------ELIMINAR---------------------------------------------------------------------"""
"""1. Usar el método remove(valor): Este método elimina la primera aparición del valor especificado de la lista.
Si el valor no está presente en la lista, se generará un error ValueError"""
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print(lista)  # Resultado: [1, 2, 4, 5]

#Removiendo un elemento de la lista por su valor NO POR INDICE!! | si el valor se repite elimina el 1ro
lista.remove("HOLA") #-> si le pasamos un elemento q no existe da una excepcion (error)
#si queremos que elimine + de uno podemos hacerlo con un for
#La diferencia con el "pop" es que le estamos diciendo q elemento queremos borrar, no el indice
#y otra diferencia es que no lo devuelve, simplemente lo borra de la lista

"""2. Usar el operador del: El operador del permite eliminar un elemento en función de su índice en la lista."""
#ELIMINANDO CON DEL
lista = [1, 2, 3, 4, 5]
del lista[2]  # Elimina el elemento en el índice 2 (3)
print(lista)  # Resultado: [1, 2, 4, 5]

del lista  # Elimina la lista completa
print(lista)  # Error: NameError: name 'lista' is not defined
"""Después de ejecutar del lista, la variable lista deja de existir y, por lo tanto,
no se puede acceder a ella posteriormente. Al intentar imprimir lista, se generará un error NameError."""

"""3. Usar el método pop(indice): Este método elimina y devuelve el elemento en la posición especificada.
Si no se proporciona un índice, se eliminará y se devolverá el último elemento de la lista. Si le indicamos -1 también y asi sucesivamente"""
lista = [1, 2, 3, 4, 5]
elemento = lista.pop(2)  #->
print(lista)    # Resultado: [1, 2, 4, 5]
print(elemento) # Resultado: 3. Es el elemento eliminado

"""4. Usar la instrucción del con rebanadas (slices): Se puede utilizar la instrucción del con rebanadas para
eliminar varios elementos de la lista en una sola operación."""
lista = [1, 2, 3, 4, 5]
del lista[1:4]
print(lista)  # Resultado: [1, 5]

"""5. El método clear() se utiliza para eliminar todos los elementos de una lista. Al llamar a clear() en una lista, esta se vacía,
es decir, se eliminan todos los elementos contenidos en ella, dejándola como una lista vacía. El método clear() no devuelve ningún valor,
simplemente modifica la lista original."""
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)  # Resultado: []

"""El método clear() es útil cuando se desea eliminar todos los elementos de una lista sin tener que eliminar la lista misma(es decir,
la variable que la referencia). Esto puede ser útil cuando se desea reutilizar la misma lista en lugar de crear una nueva desde cero."""
"---------------------------------------REVERSE AND REVERSED----------------------------------------------------------------------"
"""REVERSE es un método que se puede aplicar directamente a una lista y modifica la lista original invirtiendo su orden. Es un método in-place,
lo que significa que no devuelve una nueva lista invertida, sino que altera la lista existente."""
lista = [1, 2, 3, 4, 5]
lista.reverse() #Funciona para revertir cualquier lista
print(lista)  # Salida: [5, 4, 3, 2, 1]

"""reversed es una función incorporada en Python que toma una secuencia (como una lista, tupla o cadena) y devuelve un objeto de tipo
"reversed iterator"que permite iterar sobre la secuencia en orden inverso. No modifica la secuencia original,
sino que crea un nuevo objeto iterable. Para obtener una lista invertida, es necesario convertir el iterador en una lista utilizando
la función list(). Por ejemplo:"""

lista = [1, 2, 3, 4, 5]
lista_invertida = list(reversed(lista)) #Crea un objeto de tipo iterador, por eso se los transforma en una lista "reversed iterator"
print(lista_invertida)  # Salida: [5, 4, 3, 2, 1]

"""En resumen, reverse es un método para invertir la lista original directamente, mientras que reversed es una función para obtener un
iterador invertido que se puede convertir en una nueva lista si se desea."""
"""--------------------------------------------------------SORT AND SORTED------------------------------------------------------------------"""

""" Algunas características de la función sort() son:
1. Ordenamiento en lugar: La función sort() ordena la lista directamente, sin crear una nueva lista.
2. Orden ascendente por defecto: La función sort() ordena los elementos en orden ascendente, es decir, de menor a mayor.
3. Personalización del orden: La función sort() permite personalizar el orden de clasificación mediante el uso de argumentos
opcionales, como key y reverse."""
#Es importante tener en cuenta que la función sort() solo se puede aplicar a listas y no a otros tipos de secuencias, como tuplas o conjuntos.
#Los valores booleanos también se ordenan, los False en primer lugar y los True segundo (luego los numeros)

frutas = ['manzana', 'banana', 'pera', 'kiwi', 'naranja']
frutas.sort()  # Orden ascendente por defecto
print(frutas)  # Salida: ['banana', 'kiwi', 'manzana', 'naranja', 'pera']

frutas.sort(reverse=True)  # Orden descendente
print(frutas)  # Salida: ['pera', 'naranja', 'manzana', 'kiwi', 'banana']

frutas.sort(key=len)  # Orden por longitud de cadenas
print(frutas)  # Salida: ['kiwi', 'pera', 'banana', 'manzana', 'naranja']

"""sort es un método que se aplica a las listas y modifica la lista original en su lugar, es decir,
reordena los elementos de la lista directamente. No devuelve nada (o devuelve None), pero modifica la lista original."""

my_list = [5, 2, 8, 1, 3]
my_list.sort() #si a "my_list.sort()" le asignamos una variable y la imprimimos devuelve "None"
print(my_list) # Salida [1, 2, 3, 5, 8]

"""Si se aplica a una lista de cadenas de caracteres, las ordenará alfabéticamente en orden ascendente. Por ejemplo:"""

palabras = ['perro', 'gato', 'elefante', 'ratón']
palabras.sort()
print(palabras)  # Salida: ['elefante', 'gato', 'perro', 'ratón'] 

"""Por otro lado, sorted es una función incorporada de Python que toma una secuencia iterable (como una lista, tupla o cadena)
y devuelve una nueva lista que contiene los elementos ordenados. No modifica la secuencia original, sino que crea una nueva lista ordenada."""

my_list = [5, 2, 8, 1, 3]
sorted_list = sorted(my_list)
print(sorted_list)
"""-------------------------------------INDEX - IN - GET-------------------------------------------------------------------"""
#INDEX
#Verificando si un elemento se encuentra en la lista
lista = list(["hola", "dalto", 34, 56, 23, True])
elemento_encontrado = lista.index(56, 5) #tiene que ser totalmente igual, es decir, "5" solo no existiria
#"index(56, 5) la coma le indica al metodo que empiece a contar despues del elemento 5, la coma es opcional"

#Para obtener el indice de un elemento (unicamente si está, sino marca error)
lista = [1, "Dos", 3]
buscar = 3
print(lista.index(buscar))

#INDEX
#El método index() se utiliza para encontrar el índice de la primera aparición de un elemento en una lista.
#Toma como argumento el elemento que se desea buscar y devuelve el índice de su primera aparición.
#Si el elemento no está presente en la lista, se generará una excepción ValueError.
frutas = ['manzana', 'plátano', 'naranja', 'pera', 'manzana']
indice = frutas.index('naranja')
print(indice)  # Resultado: 2
"""-------------------------------------------------------------------------------------------------------"""
#IN
#Averiguar o buscar si un elemento está en nuestra lista. Ejecuta "True"
lista = [1, "Dos", 3]
buscar = 1
print(buscar in lista)

#Buscar elemento y buscar indice combinados
lista = [1, "Dos", 3]

buscar = 3
if buscar in lista:
    print(lista.index(buscar))
else:
    print("No está el elemento")
    
#Imprime valor booleano #¿12 está en equipo?
equipo = {10:"Paulo Dybala", 11:"Douglas Costa", 7:"Cristiano Ronaldo",17:"Mario Mandzukic"}
print(12 in equipo)
"""-------------------------------------------------------------------------------------------------------"""
#GET
#Esta forma se puede usar si no sabes si existe ese valor en el diccionario.
# Por el contrario, si estás seguro, usar la forma que se muestra abajo xd
print(equipo.get(6, "No existe")) 
"""-----------------------------------------ITEMS---------------------------------------------------------------------"""
#ITEMS pone todo dentro de una lista y a cada elemento lo encierra en una tupla. PRINCIPAL para diccionarios
mi_agenda = {"Alicia": 2222, "Roberto": 1111, "Lucia": 3333, "Andres": 5555}

for clave, valor in mi_agenda.items(): #Items parece que funciona casi igual que enumerate, necesitamos dos variables
    print(clave, valor) #una para recorrer las claves y otra para el valor. Items trransforma el dic en una lista de tuplas
    
#Mustra la clave con su valor al lado
diccionario = {'clave1': "valor1", 'clave2': "valor2", 'clave3': "valor3"}
for clave, valor in diccionario.items(): 
    print(clave, valor)
"""---------------------------------------ENUMERATE---------------------------------------------------------------------"""
#Para desempaquetar la tupla en variables separadas se utiliza la sintaxis for indice, elemento in enumerate(frutas).
#Luego, puedes imprimir las variables indice y elemento por separado para obtener el resultado deseado

#FORMA CON DOS VARIABLES
frutas = ["manzana", "naranja", "plátano", "pera", "melón"]
for indice, elemento in enumerate(frutas):
    print(indice, elemento)

#LO MISMO PERO CON NUMEROS ENTEROS
lista = [1,2,3,4,5,6,7,8]                   #ESTA FORMA NO ES COMÚN: enumerate(frutas, 1). Comienza con 1
for posicion, valor in enumerate(lista, 1): #SI LE DAMOS UN 2DO PARAMETRO COMIENZA CON ESE EN VEZ DEL INDICE (0 POR DEFECTO)
    print("El valor {0} es está en la posición {1}".format(valor,posicion)) 
    
#EN ESTA FORMA, "VALOR" CONTIENE UNA TUPLA CON LA FORMA (INDICE, ELEMNTO). CADA ELEMENTO IMPRESO ES UNA TUPLA Q CONTIENE IND Y ELEM
lista = [1,2,3,4,5,6,7,8]   
for valor in enumerate(lista):
    print(valor)

#SI QUIERO AL INDICE ES [0] Y SI QUIERO ACCEDER AL ELEMENTO ES [1] | LA FORMA MÁS COMÚN DE USAR ENUMERATE CON 2 VARIABLES
frutas = ["manzana", "naranja", "platano", "pera", "melon"]
for elemento in enumerate(frutas): #LITERALMENTE "ENUMERATE" TRANSFORMA LA LISTA EN UNA TUPLA CON (INDICE, ELEMENTO) PARA Q LA RECORRAMOS
    print(elemento[0]) #"ELEMENTO" CONTIENE LA TUPLA DE LA FORMA (INDICE, ELEM), POR ESO ES COMUN SEPARARLO EN 2 VARIABLES
###############################################################################################################################

#El código utiliza la función enumerate para iterar sobre una lista de listas listado. Cada elemento de la lista
#listado es una sublista que contiene dos elementos: un nombre y un valor numérico. En el bucle for, al utilizar
# enumerate(listado), se obtienen dos valores en cada iteración: el índice i y el elemento item.

# El índice i representa la posición del elemento en la lista, y item representa la sublista completa.
listado = [["Mary", 70.5], ["Anna", 63.8], ["Juan", 30.3]]

for i, item in enumerate(listado, start=1): #Poner "start=1" o solo el numero entero da igual, ambos casos se inicializan en ese numero
 print(i, item)
#-----IMPRIME-------
# 0 ['Mary', 70.5]
# 1 ['Anna', 63.8]
# 2 ['Juan', 30.3]
"""-------------------------------------------SUM-------------------------------------------------------------------------"""
#METODO SUM | La suma de todos los elementos de una lista compuesta unicamente con elementos numericos
#MINIMO DE UN ARGUMENTO Y UN MAXIMO DE 2 ARGUMENTOS DE MANERA SIMULTANEA | SI ES 1 ARGUMENTO ES UN OBJETO ITERABLE
numero  = [1, 2, False] #El primer argumento es un objeto iterable, puede ser lista y el segundo si o si un valor ENTERO
print(sum(numero, -2)) #comienza la suma con 10
#Los valores de tipos de booleano tienen valor entero "True" valo 1 y "False" vale 0
#SI QUEREMOS SUMAR STRINGS NOS SALTA UN TYPE ERROR XD
"""----------------------------------------MIN and MAX----------------------------------------------------------------------------"""
#La función min en Python se utiliza para encontrar el valor mínimo de una secuencia de elementos. Puede ser aplicada a
#varios tipos de secuencias, como listas, tuplas, conjuntos y cadenas de caracteres.
numeros = [5, 2, 8, 1, 9]
minimo = min(numeros)
print(minimo)  # Resultado: 1

cadena = "Hola mundo"
minimo = min(cadena)
print(minimo)  # Resultado: ' '

conjunto = {10, 5, 8, 3, 7}
minimo = min(conjunto)
print(minimo)  # Resultado: 3

#Es importante tener en cuenta que si se aplica min a un iterable vacío, se producirá un error ValueError
"----------------------------------------------------------------------------------------------------------------------------------------"



"""----------------------------KEY AND VALUES: DISEÑADO ESPECIFICAMENTE PARA DICCIONARIOS-------------------------------------------------------------------------------"""
#KEY
"""La función keys() es un método que se utiliza en Python para obtener una vista de las claves de un diccionario.
Cuando se aplica keys() a un diccionario, retorna un objeto de vista iterable que contiene todas las claves presentes en el diccionario.
Esta vista de las claves se actualiza automáticamente si se realizan cambios en el diccionario original."""

diccionario = {"a": 1, "b": 2, "c": 3}
claves = diccionario.keys()

print(claves) #dict_keys(['a', 'b', 'c'])

"""En este caso, keys() devuelve un objeto de tipo dict_keys que contiene las claves del diccionario diccionario.
La vista de las claves puede ser utilizada en bucles for o convertida a una lista o conjunto para su manipulación."""

#ITERANDOLA CON EL BUCLE FOR
diccionario = {"a": 1, "b": 2, "c": 3}

for clave in diccionario.keys(): 
    print(clave) #a, b, c (en vertical)

#CONVIRTIENDOLA EN LISTA
diccionario = {"a": 1, "b": 2, "c": 3}

clave = list(diccionario.keys()) #tambien se puede transformar en una lista, tupla o conjunto
print(clave) #['a', 'b', 'c']    #PERO no en otro diccionario

#RECORRER DICCIONARIO POR SU CLAVE
diccionario = {'clave1': "valor1", 'clave2': "valor2", 'clave3': "valor3"}
for key in diccionario: #el primer valor en for siempre es la clave
    print(diccionario[key])
"-------------------------------------------------------------------------------------------------------------------------------"
#VALUES
"""Cuando se aplica values() a un diccionario, devuelve un objeto de vista iterable que contiene todos los valores presentes en el diccionario.
Esta vista de los valores se actualiza automáticamente si se realizan cambios en el diccionario original."""

diccionario = {"a": 1, "b": 2, "c": 3}
valores = diccionario.values()

print(valores) #dict_values([1, 2, 3])

"""En este caso, values() devuelve un objeto de tipo dict_values que contiene los valores del diccionario diccionario.
La vista de los valores puede ser utilizada en bucles for o convertida a una lista o conjunto para su manipulación.

Aquí tienes un ejemplo adicional que muestra cómo se puede utilizar values() en un bucle for:"""

#ITERANDOLA CON EL BUCLE FOR
diccionario = {"a": 1, "b": 2, "c": 3}

for valor in diccionario.values():
    print(valor)
    
#CONVIRTIENDOLA EN LISTA
diccionario = {"a": 1, "b": 2, "c": 3}

valores = list(diccionario.values())
print(valores) #[1, 2, 3] 

#PODEMOS ITERAR SOBRE "VALORES"
for i in valores:
    print(i) #Muestra los valores en forma vertical
    
#Vemos si el valor "Paulo Dybala" existe en equipo como valor
equipo = {10:"Paulo Dybala", 11:"Douglas Costa", 7:"Cristiano Ronaldo",17:"Mario Mandzukic"}

if "Paulo Dybala" in equipo.values(): 
    print("Ese valor está en el diccionario.")
    
#La primera variable a recorrer siempre es la clave
mi_agenda = {"Alicia": 2222, "Roberto": 1111, "Lucia": 3333, "Andres": 5555}

for clave in mi_agenda: 
    print(clave,":", mi_agenda[clave])
"""------------------------------------------------------------------------------------------------------------------------------"""