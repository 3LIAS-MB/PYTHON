#BUCLE FOR
numeros = [2, 3, 5, 7, 11]

for i in numeros:#EN EL PRIMER CICLO LA VARIBALE "I" EXTRAE EL NUMERO Y LO IMPRIME, ASI HASTA TERMINAR, POR ESO ESTA EN VERTICAL
    print(i) #i toma el valor de numeros y lo imprime en la consola
    #se imprime verticalmente, ya no horizontal como cuando solo invocamos la variable
    
#TABLA DE MULTIPLICAR USANDO FOR
#FORMA 1
tabla = int(input("ingrese el numero a multiplicar"))

for i in range(1,11):
    resultado = tabla * i
    print(f"{tabla}x{i}= {resultado}")

#FORMA 2
numero = 7
tabla = range(1,11)

for i in tabla:
    print(f"{numero}x{i}={i*numero}") 
    
#-------------------------------------
#FORMA 3
tabla = int(input("ingrese la tabla de multiplicar: "))

for i in range(1,11):
    resultado = tabla * i   
    print(tabla,"*",i,"=",resultado) #7 * 1 = 7
    
#USANDO WHILE
tabla = int(input("ingrese un numero para multiplicar"))
inicio = 1
while inicio <= 10:
    resultado = tabla * inicio
    print(f"{tabla}x{inicio}={resultado}")
    inicio += 1
    
#Mostrar la suma y la cantidad de números pares comprendidos entre dos numeros ingresados
#por el teclado, ej.: 5 y 10

numero_inicial = int(input("ingrese el numero inicial: "))
numero_final = int(input("ingrese el numero final: "))
cantidad = 0

while numero_inicial < numero_final:
     if numero_inicial % 2 == 0:
         print(numero_inicial)
         cantidad += 1
     numero_inicial += 1
print("hay",cantidad,"numeros pares")

#Programar un bucle que cuente atrás del 5 al 1 y al final imprimir el mensaje "Despegue!"

numero = range(5, 0, -1)

for i in numero:
    print(i)
else:
    print("¡Despegue!")

#----------------break----------
#Listado de diez personas que esten en una fila, pero solo hay cupos para 8
lista = range(1, 11)

for num in lista:
    if num > 8:
        break
    print(num)
#-----------
num = 1

while num < 11:
    if num > 8:
        break
    print(num)
    num +=1
#-----------CONTINUE---------

#Se muestran los numeros del 1 al 50 con un salto de 3 y exceptuando la familia del 30

list = range(1, 50, 3)

for num in list:
    if num >= 30 and num <= 39:
        continue #continue
    print(num)
#
num = 1
while num < 50:
    if num >= 30 and num <= 39:
        num += 4
        continue
    else:
        print(num)
        num += 4
#repetidor
while True:
    palabra = input("introduce una palabra: ")
        
    if palabra ==  "salir":
        break
    
    if palabra == "rayos":
        continue
    
    print(palabra)
#####################
contador = 0
suma = 0
logico_max = True
continuar = 's'
while (continuar == 's'):
  nota = float(input('Ingrese nota:'))
  suma += nota
  contador += 1
  if logico_max:
    logico_max = False
    nota_max = nota
    pos_nota_max = contador
  else:
    if nota > nota_max:
       nota_max = nota
       pos_nota_max = contador
continuar = input('Continuar (s/n):')
promedio = suma/contador
print('Promedio: ', promedio)
print('Nota máxima: ', nota_max)
print('Posición Máximo: ', pos_nota_max)

#2
orden = 0
importe_total = 0
logico_max = True
continuar = 's'
while (continuar == 's'):
  
  while True:
    precio_unitario = float(input('Precio unitario:'))
    cantidad = int(input('Cantidad:'))
    if not precio_unitario <= 0 and not cantidad <= 0:
       break
  
  orden += 1
  importe = precio_unitario * cantidad
  if cantidad >= 5:
     importe *= 0.9
  print(f'El importe del cliente {orden} es ${importe}')

  importe_total += importe

  if logico_max:
     logico_max = False
     importe_max = importe
     pos_importe_max = orden
  else:
     if importe > importe_max:
        importe_max = importe
        pos_importe_max = orden
  continuar = input('Continuar (s/n):')

print(f'El cliente {pos_importe_max} pagó el máximo importe ${importe_max}')
print(f'El total recaudado por el supermercado es ${importe_total}')

#

def modulo_uno():
    def modulo_dos():
        global a   
        print(a)
        a = 1
        return
    
    a = 3    
    modulo_dos()
    print(a)
    return

a = 4
modulo_uno()    
print(a)