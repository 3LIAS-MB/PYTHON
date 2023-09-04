"""------------------------------------------------FUNCIONES EN PYTHON-------------------------------------------"""
"""Las funciones son un grupo de lineas de codigos que nosotros agrupamos aparte del programa
principal que forman entre ellas un mini programa que cumplen una funcion determinada"""

def cantar_coro(): #->
    print("Asereje, ja de je dejeve tu dejevere")
    print("sebinouva majabi an de bugi an de buididipi")

cantar_coro() #-> puedo llamar a la función tantas veces yo quiera
cantar_coro()
cantar_coro()

#

def saludar():
    print("Hola")
    print("¿Cómo estás?")
    print("¡Es un gusto volvera verte!")

def despedir():
    print("Espero que te la hayas pasado bien.")
    print("Adiós.")
    
saludar()
despedir()

"""---------------------------------------------PARAMETROS EN PYTHON---------------------------------------------"""

def saludar(nombre): #-> Lo que está adentro de los parentesis se llama parametro
    print("Hola, " + nombre + ".") #->Aquí pasa a ser una variable
    print("¿Cómo estás?")   
    print("¡Es un gusto volvera verte!")
    
saludar("Andrés") #->Cuando se llama a la función, se la llama con un argumento (Andrés)

"""--------------------------MULTIPLES PARAMETROS EN PYTHON: ARGUMENTOS POSICIONALES-----------------------------"""
#Aquí empresa tiene un argumento por defecto. Los argumentos por defecto tienen que ir ultimo
def saludar(nombre, apellido, empresa ="Banco MND"): #-> Así se usa varios parametros dentro de una funcion, separados por una coma
    
    print("Hola, " + nombre + " " + apellido + ".")
    print("Bienvenido a " + empresa + ".")
    print("¿Como estas?")
    print("¡Es un gusto volverte a verte!")
    
#-----ARGUMENTOS POSICIONALES-------------
saludar("Andrés", "Juarez", "Banco ABC") #-> Los argumentos tienen que coincidir con el orden de los parametros
saludar("Juan", "Torres", "Banco ELI") #->

#-----ARGUMENTOS DE PLABRA CLAVE (Keyword  arguments)---------------
saludar(empresa = "Banco  XYZ", nombre = "Daniel", apellido = "Ruiz") #Los argumentos de palabra clave sí se pueden
#poner en desorden. Si hay un argumento por defecto y también uno en palabra clave o posicional, se le da prioridad
#a los que están en el codigo #original.

"""-----------------------------------------------RETURN en PYTHON---------------------------------------------"""  
def multiplicar(a,b):
    return a*b #-> Devuelve valores de la función al programa principal

#Puedo imprimirlo de esta manera -> Lo almaceno en una variable
resultado = multiplicar(10,5) + 5 #-> Si quiero  le sumo, resto, multiplico, divido, etc, entre 5.
print(resultado)
#Puedo imprimirlo de esta manera -> Se puede imprimir directamente
print(multiplicar(10,5))
#Puedo imprimirlo de esta manera -> Lo puedo transformar en string u otro y lo concateno con un texto 
print("Mi edad es: " + str(multiplicar(5,10)))

"""--------------------------------------RETORNAR MULTIPLES VALORES--------------------------------------------"""
def cordenadasAlCuadrado(x,y):
    cordenadaX = x * x  
    cordenadaY = y * y
    return cordenadaX, cordenadaY #-> #Lo que hace return  es retornar los valores a la función principal

#El primero  "cordenada X" se asigna a la primera variable "xAlCuadrado" y asi sucesivamente
xAlCuadrado, yAlCuadrado = cordenadasAlCuadrado(1,3)
 #-> Cuando se retorna varios valores lo mejor es guardarlos en variables para poder usarlas cuando queramos
print(xAlCuadrado)
print(yAlCuadrado)
"""--------------------------------------------SCOPE -> ALCANCE---------------------------------------------------"""
def comidaEspecial(alimento): #-> NO todo el archivo puede tener acceso a la variable "alimento", solo está
    #definida dentro de la  función. Lo que está adentro no se pueda usar fuera de la función
    return texto + alimento

texto = "Nuestra comida especial de hoy es: " #-> La variable texto se puede usar en TODO el archivo
print(comidaEspecial("Salmon"))

#

def comidaEspecial(alimento):
    return "Nuestra comida especial de hoy es: " + alimento

print(comidaEspecial("pene"))