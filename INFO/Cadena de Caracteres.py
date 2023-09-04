"""----------------------------------------------FORMAT---------------------------------------------------------------------------"""
"""El método format() formatea los valores especificados y los inserta dentro del marcador de posición de la cadena. Los marcadores de posición
se pueden identificar mediante índices con nombre {precio}, índices numerados {0} o incluso marcadores de posición vacíos {}"""

txt = 'Soy {nombre}, tengo {edad} años'
print(txt.format(nombre = 'Juan', edad = 19))#Soy Juan, tengo 19 años

txt = 'Me gusta {0} y {1}'
print(txt.format('viajar','nadar'))#Me gusta viajar y nadar txt = 'Soy {} de {}' print(txt.format('estudiante','Ingeniería'))#Soy estudiante de Ingeniería

txt = 'El binario de {0} es {0:b}'
print(txt.format(5))#El binario de 5 es 101

precio = 49.0999
txt = "El precio es {:.2f} pesos"
print(txt.format(precio))#El precio es 49.10 pesos
"""--------------------------------------------RECORRER --------------------------------------------------------------------------------------"""
b = ' '
h = 'hOlA'
m = 'mUNdo'
c = input('Ingrese cadena: ') #cRuEL
s = h + b + m + b + c + b*2
#Contar blancos
cont = 0
for car in s:
    if car == b:
        cont += 1
print(f'espacios: {cont}') #4
#Contar blancos bis
cont = 0
for i in range(len(s)):
    if s[i] == b:
        cont += 1
print(f'espacios: {cont}') #4
"""----------------------------------------------CARACTERES DE ESCAPE-------------------------------------------------------------------------"""
#print('\\hola\\') \hola\
#\' Comilla simple
#\\ Backslash
#\n Nueva linea
#\r Carriage Return
#\t Tab
#\b Backspace
#\v Vertical tab
#\ooo Octal value
#\xhh Hex value
"""_-----------------------------------------REBANADAS - SLICING-----------------------------------------------------------------------------"""
"""Las rebanadas pueden tener 1, 2 o 3 parámetros str[i:f:p],
donde i es inicio, f fin (-1) y p es el paso"""

nombre = 'Juan Cruz'

print(nombre[1]) # u
print(nombre[-4]) # C
print(nombre[1:3]) # ua
print(nombre[1:-1]) # uan Cru
print(nombre[:3]) # Jua
print(nombre[2:]) # an Cruz
print(nombre[:-1]) # Juan Cru
print(nombre[::2]) # Ja rz
print(nombre[1::2]) # unCu
print(nombre[::-1]) # zurC nauJ
#nombre  J  u  a  n  -  C  r  u  z
#índice  0  1  2  3  4  5  6  7  8
#índice -9 -8 -7 -6 -5 -4 -3 -2 -1
"""--------------------------------------------METODOS------------------------------------------------------------------------------------"""
"""En Python un método es una función que es definida con
respecto a un objeto en particular. Para una cadena el
objeto es un string
La sintaxis es:"""
#<objeto>.<metodo>(<parametros>)
adn = 'ACGT'
pos = adn.find('T')
print(pos) #3
"""-------------Métodos: separar - unir: SOLO PARA STRING, PERO VALORES ENTEROS HAY QUE HACERLOS STRING-------------------------------------"""
"""-----------------------------------------------SPLIT------------------------------------------------------------------"""
"""El método split() en Python se utiliza para dividir una cadena en una lista de subcadenas en función de un delimitador.
Toma el delimitador como argumento opcional y, si no se proporciona, divide la cadena en los espacios en blanco."""

texto = "Hola, cómo estás?"
print(texto) #Hola, cómo estás?
palabras = texto.split()  # divide la cadena en espacios en blanco
print(palabras) #['Hola,', 'cómo', 'estás?']

"""También puedes proporcionar un delimitador específico como argumento para dividir la cadena en función de ese delimitador. Por ejemplo:"""

frase = "Manzana,Naranja,Pera"
frutas = frase.split(",")  # divide la cadena en comas
print(frutas) #['Manzana', 'Naranja', 'Pera']

"""-----------------------------------------------JOIN------------------------------------------------------------------"""
"""El método join() en Python se utiliza para concatenar elementos de una lista (o cualquier iterable) en una cadena de texto. Toma una lista
de cadenas como argumento y devuelve una cadena en la que los elementos de la lista están concatenados por el separador especificado.

La sintaxis general del método join() es la siguiente:"""
#cadena_separador.join(iterable)

"""Donde:

"cadena_separador" es la cadena que se utiliza como separador para unir los elementos del iterable.
"iterable" es el iterable (como una lista, tupla o conjunto) que contiene las cadenas a unir.

Aquí tienes un ejemplo para ilustrar cómo se utiliza el método join():"""
lista = ["Hola", "mundo", "en", "Python"]
cadena_unida = " ".join(lista)
print(cadena_unida)  # Output: "Hola mundo en Python"

#OTRO EJEMPLO
nombres = ["Juan", "Olivia", "Elias", "Nestor"]
formato = ' - '.join(nombres)
print(formato) #Juan, Olivia, Elias, Nestor | Juan - Olivia - Elias - Nestor

#EJEMPLO GENERAL XD
a = '192.168.0.1'.split('.')
print(a) # ['192', '168', '0', '1']
b = ['red', 'green', 'blue']
print(' '.join(b)) # red green blue
print(''.join(b)) # redgreenblue
print('***'.join(b))# red***green***blu
"""---------------------------------------METODO MAP-------------------------------------------------------------------------------------------"""
"""El método map() en Python se utiliza para aplicar una función a cada elemento de una secuencia, como una lista o una cadena.
Toma dos argumentos: la función que se aplicará y la secuencia sobre la cual se aplicará."""

#Sintaxis general
"map(función, secuencia)"

"""Cuando se utiliza map(), se crea un objeto de tipo map que contiene los resultados de aplicar la función a cada elemento de la secuencia.
Puedes convertir el objeto map en una lista o en otro tipo de secuencia para ver los resultados"""

#EJEMPLO 1
#Definimos una función que suma 1 a un número
def sumar_uno(numero):
    return numero + 1

#Creamos una lista de números
numeros = [1, 2, 3, 4, 5]

#Aplicamos la función sumar_uno a cada número de la lista utilizando map()
resultado = map(sumar_uno, numeros)

#Convertimos el objeto map en una lista para ver los resultados
lista_resultado = list(resultado)

print(lista_resultado)

#EJEMPLO 2
def contar_vocales2(texto):
    return sum(map(texto.lower().count, 'aeiouáéíóúü'))
"""--------------------------------------------------METODOS-----------------------------------------------------------------------"""
"""------------------------------------------------METODO FIND------------------------------------------------------------------------"""
"""El método find devuelve la posición (índice) de la primera aparición de la subcadena en la cadena.
Si la subcadena no se encuentra, devuelve -1. FIND distingue entre mayusculas y minisculas, si se quiere hacer una busqueda
sin distinguir entre mayusculas y minusculas se puede usar upper o lower para convertir la cadena o subcadena. SOLO PARA CADENA DE CARACTERES"""

#La sintaxis general del método find es la siguiente:
#cadena.find(subcadena, inicio, fin)

cadena = "Hola, bienvenido al mundo Python"
posicion = cadena.find("bienvenido")
print(posicion)  # Salida: 6

#"cadena" es la cadena en la que se realizará la búsqueda.

#"subcadena" es la subcadena que se desea buscar.

#"inicio" (opcional) es el índice desde el cual comenzará la búsqueda. Por defecto, es 0,
#lo que significa que la búsqueda se realizará desde el inicio de la cadena.

#"fin" (opcional) es el índice hasta el cual se realizará la búsqueda. Por defecto, es la longitud de la cadena,
#lo que significa que la búsqueda se realizará hasta el final de la cadena.

"""-----------------------------------------------METODO RFIND-------------------------------------------------------------------------"""
"""El método rfind es similar al método find en Python, pero realiza la búsqueda desde el final de la cadena en lugar de hacerlo desde el principio.
La "r" en rfind significa "reverse" (reversa). Mientras que el método find busca la primera aparición de una subcadena desde el inicio de la
cadena, el método rfind busca la última aparición de la subcadena desde el final de la cadena. Devuelve la posición de la última aparición
encontrada o -1 si no se encuentra la subcadena."""

cadena = "   Hola mundo, bienvenido al mundo Python   "
posicion = cadena.rfind("mundo")
print(posicion)  # Salida: 29

"""El método rfind es útil cuando se necesita encontrar la última aparición de una subcadena en una cadena, en lugar de la primera
aparición como lo hace el método find."""

"""----------------------------------------------METODO COUNT--------------------------------------------------------------------------------"""
"""El método count en Python se utiliza para contar el número de apariciones de una subcadena dentro de una cadena. Toma como argumento la
subcadena que se desea buscar y devuelve la cantidad de veces que esa subcadena aparece en la cadena original."""

cadena = "Hola, hola, hola, bienvenido"
contador = cadena.count("hola")
print(contador)  # Salida: 2

cadena = "Hola, hola, hola, bienvenido"
contador = cadena.count("hola")
print(contador)  # Salida: 2

#El método count también puede aceptar un segundo argumento opcional para especificar el índice inicial y final dentro de la
#cadena donde se realizará la búsqueda. Por ejemplo:

cadena = "Hola, hola, hola, bienvenido"
contador = cadena.count("hola", 5, 15)
print(contador)  # Salida: 2

"""----------------------------------------------CAPITALIZE-------------------------------------------------------------------"""
"""El método capitalize() en Python se utiliza para convertir el primer carácter de una cadena en mayúscula,
y el resto de la cadena en minúsculas."""

cadena = "hola, bienvenido"
capitalizada = cadena.capitalize()
print(capitalizada) #Hola, bienvenido

"""-----------------------------------------------LOWER--------------------------------------------------------------------"""
"""El método lower() en Python se utiliza para convertir todos los caracteres de una cadena en minúsculas."""
cadena = "Hola, Bienvenido"
minusculas = cadena.lower()
print(minusculas) #hola, bienvenido

"""---------------------------------------------UPPER-------------------------------------------------------------------"""
"""El método upper() en Python se utiliza para convertir todos los caracteres de una cadena en mayúsculas."""
cadena = "Hola, Bienvenido"
mayusculas = cadena.upper()
print(mayusculas) #HOLA, BIENVENIDO

"""-------------------------------------------SWAPCASE-----------------------------------------------------------------"""
"""El método swapcase() en Python se utiliza para intercambiar las mayúsculas por minúsculas y viceversa en una cadena."""
cadena = "HoLA, bIEnvenido"
cambiada = cadena.swapcase()
print(cambiada) #hOlA, BienVENIDO

"""-----------------------------------------TITLE----------------------------------------------------------------------"""
"""El método title() en Python se utiliza para convertir la primera letra de cada palabra en una cadena en mayúscula
y el resto de las letras en minúscula, asumiendo que las palabras están separadas por espacios."""
cadena = "bienvenidos al tutorial de python"
titulo = cadena.title()
print(titulo) #Bienvenidos Al Tutorial De Python

#MAS EJEMPLOS
s = 'hOlA mUNdo cRuEL '
s.find('m') #5
s.rfind('u') #11
s.find('el') #-1
s.count(' ') #4
s.capitalize() #'Hola mundo cruel '
s.lower() #'hola mundo cruel '
s.upper() #'HOLA MUNDO CRUEL '
s.swapcase() #'HoLa MunDO CrUel '
s.title() #'Hola Mundo Cruel '
"""-------------------------------------------METODOS: SOLO PARA CADENAS-----------------------------------------------------------------"""
"""------------------------------------------------CENTER-------------------------------------------------------------------------------"""
"""El método center() en Python se utiliza para centrar una cadena de texto (string) añadiendo espacios o caracteres segun nosotros le
indiquemos, tanto al inicio y al final del string, para posteriormente mostrarnos el mismo string, pero con los cambios realizados
Toma dos argumentos, pero podemos trabajar solo con el primero. Recordar que el ancho puede ser una variable con valor entero

La sintaxis general del método center() es la siguiente:"""

#cadena.center(ancho, carácter_relleno) | No se pueden poner dos caracteres y el primer argumento tiene que ser un numero entero

string = "menu"
print(string.center(10, "=")) #==menu==

string = "menu"
string = string.center(6, "=")
print(string) #=menu=

"""
"cadena" es la cadena de texto que se desea centrar.
"ancho" es el ancho total deseado para el campo centrado, se rellena a los costados
"carácter_relleno" es un carácter opcional que se utilizará como relleno. Por defecto, se utiliza un espacio en blanco."""

"""------------------------------------------------------Ijust----------------------------------------------------------------------------"""
"""El metodo Ijust(), nos permite alinear un Sting a la izquierda, añadiendo espacios o caracteres segun nosotros le indiquemos, unicamente
al final del string, para posteriormente mostrarnos el mismo string pero con los cambios realizados"""

#La sintaxis para el metodo "Ijust()" es:

#nombre_variable.Ijust(esp_izquierda, "=") | No se pueden poner dos caracteres y el primer argumento tiene que ser un numero entero

string = "menu"
ancho = 10
print(string.ljust(ancho, "=")) #menu======

"""-----------------------------------------------Rjust-----------------------------------------------------------------------------"""
"""El metodo 'rjust()' nos permite alinear un string a la derecha, añadiendo espacios o caracteres segun nosotros le indiquemos,
unicamente al unicio del string, para posteriormente mostrarnos el mismo string pero con los cambios realizados"""

#La sintaxis para el metodo "rjust()":

#nombre_variable.rjust(esp_derecha, "=")

string = "menu"

print(string.rjust(10, "=")) #======menu

"""------------------------------------------------zfill------------------------------------------------------------------------------------"""
"""El método zfill() en Python se utiliza para rellenar una cadena de texto numérica con ceros a la izquierda hasta alcanzar una longitud
especificada. El objetivo principal del método es agregar ceros a la izquierda de una cadena numérica para que tenga una longitud uniforme."""

#La sintaxis general del método zfill() es la siguiente:

#cadena.zfill(longitud)

cadena = "42"
longitud = 6
cadena_rellenada = cadena.zfill(longitud)

print(cadena_rellenada) #000042

"""---------------------------------------------replace---------------------------------------------------------------------------"""
"""El método replace() en Python se utiliza para reemplazar todas las apariciones de un determinado substring o patrón en una cadena
con otro substring o patrón especificado.

La sintaxis general del método replace() es la siguiente:"""

#cadena.replace(substring_a_reemplazar, nuevo_substring, contador)

"""cadena es la cadena original en la cual se realizará el reemplazo.
substring_a_reemplazar es el substring o patrón que se desea reemplazar.
nuevo_substring es el substring o patrón que se utilizará para reemplazar las apariciones del substring_a_reemplazar.
contador (opcional) es el número máximo de reemplazos que se realizarán. Si se omite, se reemplazarán todas las apariciones."""


"""El método replace() retorna una nueva cadena con las apariciones del substring_a_reemplazar reemplazadas por el nuevo_substring.
Es importante destacar que el método replace() no modifica la cadena original, sino que crea una nueva cadena con los cambios realizados.

Aquí hay un ejemplo para ilustrar su uso:"""
cadena = "Hola mundo!"
nueva_cadena = cadena.replace("mundo", "Python")
print(nueva_cadena) #"Hola Python!"

"""---------------------------------------lstrip(), rstrip, strip----------------------------------------------------------------------------"""
"""Los métodos lstrip(), rstrip() y strip() se utilizan para eliminar caracteres espaciales (espacios en blanco, tabulaciones, saltos de línea)
de una cadena al inicio (lstrip()), al final (rstrip()) o tanto al inicio como al final (strip()).

Aquí te explico brevemente la función de cada uno:

lstrip(): Este método elimina los caracteres espaciales del lado izquierdo (inicio) de una cadena y devuelve la cadena resultante.
Es útil cuando se quiere eliminar los espacios en blanco u otros caracteres al inicio de una cadena.

rstrip(): Este método elimina los caracteres espaciales del lado derecho (final) de una cadena y devuelve la cadena resultante.
Es útil cuando se quiere eliminar los espacios en blanco u otros caracteres al final de una cadena.

strip(): Este método elimina los caracteres espaciales tanto del lado izquierdo como del lado derecho (inicio y final) de una cadena y
devuelve la cadena resultante. Es útil cuando se quiere eliminar los espacios en blanco u otros caracteres al inicio y al final de una cadena.

A continuación, te muestro un ejemplo de cómo se pueden utilizar estos métodos:"""

cadena = "   Hola mundo!   "

# Utilizando lstrip() para eliminar espacios al inicio
cadena_lstrip = cadena.lstrip()
print(cadena_lstrip)  # Output: "Hola mundo!   "

# Utilizando rstrip() para eliminar espacios al final
cadena_rstrip = cadena.rstrip()
print(cadena_rstrip)  # Output: "   Hola mundo!"

# Utilizando strip() para eliminar espacios al inicio y al final
cadena_strip = cadena.strip()
print(cadena_strip)  # Output: "Hola mundo!"

"""Los métodos lstrip(), rstrip() y strip() no toman argumentos obligatorios. Sin embargo, pueden recibir un argumento opcional que especifica
los caracteres que se deben eliminar en lugar de los espacios en blanco predeterminados."""
"""----------------------------------------------------.isdigit()---------------------------------------------------------------------------"""
"""El método .isdigit() es un método de cadena en Python que se utiliza para verificar si una cadena contiene solo caracteres numéricos.
Retorna True si todos los caracteres de la cadena son dígitos (0-9), y False en caso contrario."""

#Aquí hay algunos ejemplos de uso del método .isdigit

cadena1 = "12345"
print(cadena1.isdigit())  # Output: True

cadena2 = "abc123"
print(cadena2.isdigit())  # Output: False

cadena3 = "9876.54"
print(cadena3.isdigit())  # Output: False

cadena4 = "42"
print(cadena4.isdigit())  # Output: True

#ES DE TIPO STR Y POR ELLO HAY QUE CONVERTIR LOS ENTEROS EN CADENA

numero_entero = 12345
cadena = str(numero_entero)
print(cadena.isdigit())  # Output: True

"""----------------------------------------------------.isalnum()---------------------------------------------------------------------------"""
"""El método isalnum() en Python es utilizado para verificar si todos los caracteres de una cadena son alfanuméricos.
Devuelve True si todos los caracteres son alfanuméricos (letras o números), y False en caso contrario.

Aquí tienes un ejemplo:"""

cadena1 = "Hola123"
cadena2 = "Hola 123"
cadena3 = "Hola!"
print(cadena1.isalnum())  # Output: True
print(cadena2.isalnum())  # Output: False -> porque hay un espacio
print(cadena3.isalnum())  # Output: False -> porque hay signode exclamacion
#SI LA CADENA ESTA VACIA TAMBIEN DEVUELVE FALSE

"""----------------------------------------------------".isalpha()---------------------------------------------------------------------------"""
"""El método isalpha() en Python se utiliza para verificar si todos los caracteres de una cadena son letras del alfabeto.
Devuelve True si todos los caracteres son letras y la cadena no está vacía, y False en caso contrario.

Aquí tienes un ejemplo:"""

cadena1 = "Hola"
cadena2 = "Hola123"
cadena3 = "123"
print(cadena1.isalpha())  # Output: True
print(cadena2.isalpha())  # Output: False -> tiene letras pero tambien numeros
print(cadena3.isalpha())  # Output: False -> numeros
#SI LA CADENA ESTA VACIA TAMBIEN DEVUELVE FALSE
"""----------------------------------------------------.islower() ---------------------------------------------------------------------------"""
"""El método islower() en Python se utiliza para verificar si todos los caracteres de una cadena están en minúsculas.
Devuelve True si todos los caracteres son letras minúsculas y la cadena no está vacía, y False en caso contrario."""

#Aquí tienes un ejemplo:

cadena1 = "hola"
cadena2 = "Hola"
cadena3 = "123"
print(cadena1.islower())  # Output: True
print(cadena2.islower())  # Output: False -> contiene letra mayusculas
print(cadena3.islower())  # Output: False -> contiene numeros
#SI LA CADENA ESTA VACIA TAMBIEN DEVUELVE FALSE
"""----------------------------------------------------.isupper() ---------------------------------------------------------------------------"""
"""El método .isupper() es un método de cadena en Python que se utiliza para verificar si todos los caracteres de una cadena están en mayúsculas.
Retorna True si todos los caracteres de la cadena son letras mayúsculas y no contiene ningún otro tipo de caracteres, como dígitos,
espacios o símbolos. Retorna False en caso contrario."""

cadena1 = "HOLA"
cadena2 = "Hola"
cadena3 = "12345"
cadena4 = "HOLA123"
cadena5 = "HOLA!"

print(cadena1.isupper())  # True
print(cadena2.isupper())  # False
print(cadena3.isupper())  # False
print(cadena4.isupper())  # True -> como todas las letras son mayusculas retorna true
print(cadena5.isupper())  # True -> tiene un signo de exclamacion pero todas las letras son mayus por eso retorna true


"""----------------------------------------------------.istitle()---------------------------------------------------------------------------"""

"""El método .istitle() en Python se utiliza para verificar si una cadena está en formato de título.
Devuelve True si la cadena cumple con las siguientes condiciones:"""

#La primera letra de cada palabra está en mayúscula.
#Todas las demás letras de las palabras están en minúscula.
#Las palabras están separadas por espacios.
#Si la cadena cumple con estas condiciones, el método .istitle() devuelve True. En caso contrario, devuelve False.

#Aquí tienes un ejemplo:

cadena1 = "Hola Mundo"
cadena2 = "Hola mundo"
cadena3 = "Hola 123"
print(cadena1.istitle())  # Output: True
print(cadena2.istitle())  # Output: False
print(cadena3.istitle())  # Output: False
#SI LA CADENA ESTA VACIA TAMBIEN DEVUELVE FALSE
"""----------------------------------------------------.isspace() ---------------------------------------------------------------------------"""
"""El método .isspace() en Python se utiliza para verificar si una cadena está compuesta únicamente por caracteres de espacio en blanco.
Devuelve True si todos los caracteres de la cadena son espacios en blanco, y False en caso contrario.

Los caracteres considerados como espacios en blanco incluyen el espacio ' ', la tabulación '\t',
el salto de línea '\n', el retorno de carro '\r' y otros caracteres especiales de espacio en blanco."""

#Aquí tienes algunos ejemplos:

cadena1 = " "
cadena2 = "Hola Mundo"
cadena3 = "\t\n\r"
print(cadena1.isspace())  # Output: True
print(cadena2.isspace())  # Output: False
print(cadena3.isspace())  # Output: True
#SI LA CADENA ESTA VACIA TAMBIEN DEVUELVE FALSE
"""----------------------------------------------------.startswith()-------------------------------------------------------------------------"""
"""El método startswith(sub) se utiliza para comprobar si una cadena comienza con una determinada subcadena X.
Devuelve True si la cadena empieza con el subcadena especificado, y False en caso contrario.

Aquí tienes un ejemplo:"""

cadena = "Hola Mundo"
print(cadena.startswith("Hola"))  # Output: True
print(cadena.startswith("Mundo"))  # Output: False


"""El método startswith(sub) es sensible a mayúsculas y minúsculas, lo que significa que "Hola" y "hola" se considerarían diferentes subcadenas.
Si deseas hacer una comparación sin distinguir entre mayúsculas y minúsculas, puedes convertir tanto la cadena como el subcadena a minúsculas
o mayúsculas antes de realizar la verificación."""

cadena = "Hola Mundo"
print(cadena.lower().startswith("hola"))  # Output: True

"""En este caso, convertimos tanto la cadena como el subcadena a minúsculas utilizando el método .lower(), y luego verificamos si la
cadena comienza con "hola". El resultado sería True porque ahora la comparación no distingue entre mayúsculas y minúsculas."""
"""----------------------------------------------------.endswith()-------------------------------------------------------------------------"""
"""El método endswith() en Python se utiliza para verificar si una cadena termina con un sufijo específico.
Toma como argumento el sufijo que se desea comprobar y devuelve True si la cadena termina con ese sufijo, y False en caso contrario."""

#La sintaxis básica del método endswith() es la siguiente:

#cadena.endswith(sufijo)

#Aquí tienes un ejemplo para ilustrar su uso:
cadena = "Hola, mundo!"

#Comprobar si la cadena termina con "mundo!"
if cadena.endswith("mundo!"):
    print("La cadena termina con 'mundo!'")
else:
    print("La cadena no termina con 'mundo!'")

#Comprobar si la cadena termina con "Hola"
if cadena.endswith("Hola"):
    print("La cadena termina con 'Hola'")
else:
    print("La cadena no termina con 'Hola'")

