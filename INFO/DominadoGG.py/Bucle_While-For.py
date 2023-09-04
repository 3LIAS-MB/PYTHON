"""---------------------------------BLUCLE FOR------------------------------------"""
secuencia = 0
intrucciones = 0

for variable in secuencia: #la variable va a tomar el valor q le
    intrucciones           #corresponde a la secuencia
    
#Recorriendo la lista animales
animales = ["gato", "perro", "loro", "cocodrilo", "pez"]

for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}") #Se imprime todo en vertical
    print(animales) #-> Se imprime en horizontal
    
#Recorriendo la lista numeros y multiplicando cada valor por 10
numeros = [5,6,7,8,9]

for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#------¿COMO ITERAR MÁS DE 1 LISTA AL MISMO TIEMPO?------
#FOR ADENTRO DE OTRO FOR (ANIDADO)
#DOS FOR JUNTOS
#FUNCION ZIP
    
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#SE ITERA TODO AL MISMO TIEMPO, POR LO QUE SALE DESORDENADO

"""-------------------------------ITERANDO CON "RANGE"------------------------------"""
for num in range(5,10): 
    print(num)
#el primer parametro es de donde a rranca y el segundo donde termina, el ultimo no está incluido
#si ponemos un solo parametro arranca desde el cero hasta el numero que le digamos

"""---------------------------------BLUCLE WHILE--------------------------------------"""
#creando un contador que va a ir sumandose
contador = 0
#mientras que la condicion se cumpla el bucle se va a ejecutar//vuelta tras vuelta se verifica la condicion
while contador < 16:
    contador += 1
    print(contador)
#WHILE: el cilco funiona hasta que la condicion ya no se cumpla, es decir, que sea falso.
#>>>>>entra verdadero y sale falso<<<<<<<<<<