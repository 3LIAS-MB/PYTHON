#ITERAR NORMALMENTE
nombre = ["Mary", "Juan", "Anna"]
for i in range(len(nombre)):
 print(i, nombre[i])
#ITERAR DE ATRÁS PARA ADELANTE CON LA FUNCÍON REVERSE 
nombre = ["Mary", "Juan", "Anna"]
for i in reversed(range(len(nombre))):
    print(i, nombre[i])
#RECORRER NORMALMENTE
nota = [70.5, 63.8, 30.3]
for i in range(len(nota)):
 print(i, nota[i])
#RECORRER AL REVÉS
nota = [70.5, 63.8, 30.3]
for i in reversed(range(len(nota))):
 print(i, nota[i])
#RECORRER AMBOS
nota = [70.5, 63.8, 30.3]
nombre = ["Mary", "Juan", "Anna"]
for i in range(len(nombre)):
 print(i, nombre[i], nota[i])

#ITERAR SOBRE LOS ELEMENTOS DE UNA LISTA UTILIZANDO BUCLE FOR Y RANGE(LEN())
lista = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(lista)):
    print(lista[i])
 
#"pos" es el indice y "elem" el elemento (elemento que contiene lista de listas)
b = [3, 1]
c = [1, 4, b]
a = [2, 1]
x = [1, a, c, 5]
for pos, elem in enumerate(x):
    print(pos,elem)
    
#ITERAR SOBRE UNA LISTA DE LISTAS (MATRIZ)
b = [[9, 6, 4],[5, 7, 7]] #El primer bucle for i in range(len(b)) itera sobre las filas de la matriz.
                          #El segundo bucle for j in range(len(b[0])) itera sobre las columnas de la matriz. len(b[0])
for i in range(len(b)): #Devuelve la longitud de la lista "b" que es el numero de filas en la matriz (son 2)
    for j in range(len(b[0])): #Devuelve el indice de la matriz
        print(b[i][j],end='') #se usa para evitar que se agregue un salto de línea después de imprimir cada elemento en una fila.
    print()
    
#ITERAR SOBRE LA MISMA LISTA PERO DE OTRA MANERA (SI SE USA)
b = [[9, 6, 4],[5, 7, 7]]

for elem in b:
    print(elem)
    
#ITERA SOBRE TODA LA MATRIZ
d = [[5, 4, 7, 3], [4, 8, 9, 7], [5, 1, 2, 3], [4, 1, 2, 9], [6, 7, 8, 0]]
d[3][2] = 8 #para cambiar el valor de un elemento de la matriz
for i in range(len(d)):
    for j in range(len(d[0])):
        print(d[i][j],end=' ')
    print()
    
#CREAR UNA LISTA VACIA Y LE ASIGNO ALEMENTOS CON EL METODO "APPEND"
lista = ['d', 'c', 'e', 'a', 'c', 'f'] #espectativa

def cargar1():
    lista = [] #creo una lista vacia
    n = int(input('cantidad:')) 
    for i in range(n): #recorro n
        item = input('ítem:') 
        lista.append(item) #agrego "item" a "lista"
    return lista #retorno la nueva lista

lst1 = cargar1() #asigno la variable "lst1" a la funcíón retornada
print(lst1) #imprimo lst1

#OTRA FORMA PARA CREAR UNA LISTA VACIA Y AGREGARLE ELEMENTOS
def cargar2():
    lista = []
    item = input('ítem ('') fin:')
    while (item !=' '):
        lista.append(item)
        item = input('ítem ('') fin:')
    return lista

lst2 = cargar2()
print(lst2)
"----------------------------------------------------------"
#BUSCA K E IMPRIME EL INDICE EN EL QUE SE ENCUENTRA
def buscar1(lista,k):
 pos = -1
 n = len(lista)
 for i in range(n):
    if lista[i] == k: #Si no encuentra un valor igual a K en la lista
        pos = i       #nunca pasa a la condicion y pos se retorna como -1
 return pos

#ORIGINAL
lista = [10, 20, 30, 40, 50, 20] #Si hay dos numeros repetidos imprime el ultimo
k = 20
a = buscar1(lista,k)
print(a)
"----------------------------------------------------------"
#OTRA FORMA PARA BUSCAR K
def buscar2(lista,k):
 pos, i = -1, 0
 n = len(lista)
 while (i < n) and (pos == -1):
    if lista[i] == k:
        pos = i
    else:
        i += 1
 return pos

#ORIGINAL
lista = [10, 20, 30, 40, 50, 20]
k = 40
print(buscar2(lista,k))
"_-----------------------------------------------------------------"
#OTRA FORMA XD
def buscar3(lista,k):
 pos = -1
 for i,item in enumerate(lista):
    if item == k:
        pos = i
    break
 return pos

#ORIGINAL
lista = [10, 20, 30, 40, 50, 20]
k = 40
buscar3(lista, k)
"_----------------------------------------------------------------------"
