"""--------Formas clásicas de finalización del ciclo-------"""

#Finalizar por pedido del operador
#Acumular valores y contarlos
acumulador = 0.0
contador = 0
continuar = 's'
while (continuar == 's'):
  valor = float(input('Ingrese valor: '))
  acumulador = acumulador + valor
  contador = contador + 1
  continuar = input('Desea continuar (s/n): ')
print('Total: ', acumulador)
print('Cantidad: ', contador)

#Finalizar por variable lógica
#Acumular valores y contarlos.
acumulador = 0.0
contador = 0
valor = float(input('Ingrese valor (0) terminar: '))
diferenteCero = (valor != 0.0)
while diferenteCero:
  acumulador = acumulador + valor
  contador = contador + 1
  valor = float(input('Ingrese valor (0) terminar: '))
  diferenteCero = (valor != 0.0)
print('Total: ', acumulador)
print('Cantidad: ', contador)

#Finalizar por valor de salida
#Acumular valores y contarlos
acumulador = 0.0
contador = 0
valor = float(input('Ingrese valor (0) terminar: '))
while (valor != 0.0): # 0.0 valor de salida
 acumulador = acumulador + valor
 contador = contador + 1
 valor = float(input('Ingrese valor (0) terminar: '))
print('Total: ', acumulador)
print('Cantidad: ', contador)

#Finalizar por cantidad de repeticiones
#Acumular n cantidad de valores

acumulador = 0.0
contador = 0
n = int(input('Ingrese cantidad de valores: '))
while (contador < n):
 valor = float(input('Ingrese valor: '))
 acumulador = acumulador + valor
 contador = contador + 1
print('Total: ', acumulador)
print('Cantidad: ', contador)
#---------------
clave = "123"
c = 0
while True:
  c1 = input("Dame la palabra clave: ")
  if c1 == clave:
    print("Le atinaste")
    break
  else:
    print('Incorrecto')
  c += 1
  if c >= 3:
    break