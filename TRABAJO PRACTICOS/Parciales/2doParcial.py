"""2DO PARCIAL DE INTRO 2022

Se cuenta con una lista A cargada con la información de las materias de una carrera universitaria
privada donde, para cada una de ellas. se registra el código, nombre, año de cursada (1 a 5),
precios, cupo (valor entero que representa la cantidad máxima de alumnos a inscribir), y cantidad
de inscriptos actuales. Diseñar los módulos necesarios para resolver lo siguiente:

1. (30 PUNTOS) Realizar la inscripción de un alumno en una materia. Para ello, se debe
solicitar y guardar el código de materia, DNI y nombre de alumno en la lista B. Para hacer
la inscripción se debe validar que el código de materia exista en la lista A y que el cupo
máximo de la misma no se haya superado; en caso contrario en caso contrario informar con
el mensaje correspondiente. A medida que se realiza una nueva inscripción es necesario
actualizar la cantidad de inscriptos de la materia en la lista A.
2. (15 PUNTOS) A partir de la información de la lista A, Mostrar el importe total recaudado por
una materia Dando su código. Para el cálculo se debe considerar la cantidad total de
alumnos que se inscribieron en la misma.
3. (20 PUNTOS) crear una lista C que contenga la información de las materias cuyo precio sea
menor al precio promedio de todas las materias.
4. (15 PUNTOS) Informar la cantidad de alumnos cuyo nombre contenga las subcadena
“María”
5. (20 PUNTOS) Disminuir el precio de todas las materias de primer año en un 5%
importante solo debe diseñar los módulos necesarios e incluir las llamadas con el mismo desde el
programa principal coma no debe diseñar el menú de opciones debe trabajar con lista anidadas y
considere la siguiente guía para el análisis de problemas"""

#lista de materias
#[codigo, nombre, año, cantidadmax, precio, inscripto]
M1= [1001, "FISICA1", 1, 30, 1000, 30]
M2= [1002, "ALGEBRA1", 1, 30, 1000, 5]
M3=[2003, "ALGEBRA2", 2, 25,2000,5]
M4=[2004, "PROBABILIDAD", 2,25,2000,0]
M5= [3001, "ECONOMIA", 3, 15, 3000, 0]

listaA= [M1, M2, M3, M4, M5]

#lista de inscripto
#[cod_materia, dni, nombre]
Alum1= [1001,42342353, "juan Perez"]
Alum2= [1002, 41232973, "sofia cruz maria"]
Alum3  = [2003,4234464, "gustavo lopez"]
Alum4= [2004, 40235464, "lucas arias"]
listaB = [Alum1, Alum2, Alum3, Alum4 ]

def inscribir_alumno():
    codigo = int(input("Ingresar el codigo de la materia: "))
    if not validar_codigo(codigo):
        print("Error: El codigo de materia no existe")
        return
    
    if not validar_cupo(codigo):
        print("Error: El cupo esta lleno")
        return  

    dni = int(input("Ingresar DNI: "))
    alumno = input("Ingrese nombre del alumno: ")
    listaB.append([codigo, dni, alumno])

    for elemento in listaA:
        if elemento[0] == codigo:
            elemento[5] += 1
        
#VALIDACIONES
def validar_codigo(codigo):
    existe = False
    for cod in listaA:
        if codigo == cod[0]:
            existe = True
            return existe
    return existe

def validar_cupo(codigo):
    existe = False
    for cup in listaA:
        if codigo == cup[0]:
            if cup[5] < cup[3]:
                existe = True
                return existe
    return existe

def importe_total():
    total = 0
    codigo = int(input("Ingrese el codigo de la materia para ver el importe total: "))
    for i in listaA:
        if codigo == i[0]:
            total = i[4] * i[5]
    print("El total recaudado es:",total)
  
def precio_menor_alpromedio():
    listaC = []
    suma = 0
    for i in listaA:
        # sumar = sum(i[4]) esto no se puede hacer porque "sum" suma un objeto iterable, no un solo numero "i[4]"
        suma += i[4]
        promedio = suma / len(listaA)
    
    for j in listaA:
        if j[4] < promedio:
            listaC.append(j[1])
    
    print("El promedio es:",promedio)
    print("Las materias con un precio menor al promedio son:",listaC)

def sub_cadena():
    cantidad = 0
    subcadena = "Maria"
    for sub in listaB:
        if subcadena.lower() in sub[2].lower():
            cantidad += 1
    print(f"Los nombres con la subcadena 'Maria', son: {cantidad}")

def disminuir_precio():
    for dis in listaA:
        if dis[2] == 1:
            dis[4] = dis[4]*(1 - 0.05)
            
#ORIGINAL
inscribir_alumno()
importe_total()
precio_menor_alpromedio()
sub_cadena()
disminuir_precio()

for indice, valor in enumerate(listaA):
    print(indice, valor)
    
#TEMA 1, PARCIAL INTRODUCCION A LA INFORMATICA 2021

"""Dadas las listas A y B donde:

- Ambas listas guardan datos de empleados de una fabrica y pueden tener longitudes diferentes
- Paara cada empleado se registra Numero de legajo (string), Nombre (string), Salario (float)
- Debe trabajar con listas anidadas

Ejemplo del contenido de las listas: """

listaA = [['100', 'Juan Perez', 80670.29],
          ['200', 'María López', 100130.88],
          ['600', 'Jorge Munoz', 180790.00],
          ['300', 'Anna Loaiza', 89500.99],
          ['400', 'Tomas Araoz', 130200.7611]]

listaB = [['300', 'Anna Loaiza', 89500.99],
          ['600', 'Jorge Muñoz', 180790.00],
          ['100', 'Juan Perez', 80670.29],
          ['500', 'Paula Stair', 107000.50]]

"""Diseñe los modulos que resuelvan lo siguiente: 
1. Agregar a la lista A todos los empleados que tambien se encuentren en la listaB (buscando por legajo) y que su salario en la listaB sea
menor a un valor ingresado por el usuario. Por cada valor ingresado preguntar al usuario si confirma elagregado  (40 puntos)

2. Eliminar de la listaA al empleado cuyo salario sea el maximo (20 puntos)

3. A todos los empleados de la listaB cuyo salario sea mayor al promedio de salarios de la listaA, restarle 1000$ siempre que sea posible,
y si no es posible, emitir un mensaje 'Salario insuficiente para realizar la operacion' (20 puntos)"""

def agregar_x_legajo():
    legajo = input("Ingrese el legajo de la listaB que quiera agregar: ")
    salario = float(input("Ingrese un salario límite: "))
    for agregar in listaB:
        if agregar[0] == legajo:
            if agregar[2] <= salario:
                respuesta = input(f"¿Desea agregar a {agregar[1]}? (s/n): ")
                if respuesta.lower() == "s":
                    listaA.append(agregar)
                    print("\nAgregado exitosamente.")
                else:
                    print("\nCancelado exitosamente.")
                break

def eliminar_salariom_max():
    valor_max = float("-inf")
    indice = -1
    for i, salario in enumerate(listaA):
        if salario[2] > valor_max:
            valor_max = salario[2]
            indice = i
    if indice != -1:
        del listaA[indice]
        print(f"Se eliminó al empleado con un salario de {valor_max}")
    else:
        print("No se encontró un empleado con salario máximo.")

def restar_salariom_max():
    suma = 0
    for salario in listaA:
        suma += salario[2]
    promedio = suma / len(listaA)

    for empleado in listaB:
        if empleado[2] > promedio:
            if empleado[2] >= 1000:
                empleado[2] -= 1000
            else:
                print(f"Error: no es posible restarle más al empleado {empleado[1]}.")
                break

def mostrar():
    print("Lista A:")
    for i, valor in enumerate(listaA):
        print(i, valor)
    print()

    print("Lista B:")
    for i, valor in enumerate(listaB):
        print(i, valor)

agregar_x_legajo()
eliminar_salariom_max()
restar_salariom_max()
mostrar()

#TEMA 2
"""Dada la lista A y B donde:
- Ambas listas guardan datos de un colegio y pueden tener longitudes diferentes
- Para cada estudiante se registra legajo (int), nombre (string), nota(float)
- Debe trabajar con lista Anidada

Diseñe los modulos y resuleva lo siguiente:

1. Modificar en la listaA la nota de todos los estudiantes que también se
encuentre en la lista B, asignándoles la mayor nota entre ambas listas y emitir
un mensaje “Se ha modificado la nota” (40 puntos)

2. A todos los estudiantes de la lista A cuya nota sea menor al promedio de las notas
de la lista B aumentarles 5 puntos siempre que no supere la nota 10, si supera
la nota 10 debe emitir un mensaje 'no es posible realizar la operacion' (20 puntos)

3. Eliminar de la lista B, el estudiante cuya nota sea el maximo (20 puntos)

EJEMPLO DEL CONTENIDO DE LA LISTA:"""

listaA = [[100, 'Juan Perez', 8.0], 
          [200, 'María López', 7], 
          [600, 'Jorge Munoz', 10.0],
          [300, 'Anna Loaiza', 4.5],
          [400, 'Tomas Araoz', 3.5]]

listaB = [[300, 'Anna Loaiza', 5], 
          [600, 'Jorge Muñoz', 10.0], 
          [100, 'Juan Perez', 8.5], 
          [500, 'Paula Stair', 6.5]]

def modificar_nota():
    for i in listaA:
        for j in listaB:
            if i[1] == j[1]:
                if j[2] > i[2]:
                    i[2] = j[2]
                            
    print("Nota modificada correctamente!")
    
def aumentar_puntos():
    suma = 0
    contador = 0
    for nota in listaB:
        suma += nota[2]
        contador += 1
    promedio = suma / contador
    
    for estudiantes in listaA:
        if estudiantes[2] < promedio:
            if estudiantes[2] <= 5:
                estudiantes[2] += 5
            else:
                print(f"No es posbile realizar la operacion con {estudiantes[1]}.")
            
def eliminar_estudiante():
    valor = 0
    indice = 0
    for i, elemento in enumerate(listaB):
        if elemento[2] > valor:
            valor = elemento[2]
            indice = i
    del listaB[indice]
    print(f"Eliminado correctamente a {listaB[indice][1]}")      

#ORIGINALs
modificar_nota()
aumentar_puntos()
eliminar_estudiante()

legajos = [1, 2, 3, 4, 5]
nombres = ["elias", "nuwa", "martin", "sammi", "joaco"]
notas = ["elias", "nuwa", "martin", "sammi", "joaco"]

lista = [legajos+nombres+notas]
litsa = [[1, 2, 3, 4, 5], ["elias", "nuwa", "martin", "sammi", "joaco"], ["elias", "nuwa", "martin", "sammi", "joaco"]]

# def registro():
#     listado = []
#     for leg , nom, nota in zip(legajos, nombres, notas):
#         lista = []
#         lista.append(leg)
#         lista.append(nom)
#         lista.append(nota)
#         listado.append(lista)
#     print("Lista creada exitosamente!")
#     return listado

# def registro():
#     listado = []
#     for leg, nom, nota in zip(legajos, nombres, notas):
#         lista = [leg, nom, nota]  # Crear lista con los elementos correspondientes -> esta lista siempre se actualiza
#         listado.append(lista)  # Agregar la lista al listado final
#     print("Lista creada exitosamente!")
#     return listado

#PARCIAL 12/06/23 TEMA 1

def registro():
    listado = []
    for leg, nom, nota in zip(legajos, nombres, notas):
        listado.append([leg, nom, nota]) #-> INTERESANTE, se puede crear una lista adentro del parametro del append y asi añadirla a otra para hacer una lista de listas xD
    print("Lista creada exitosamente!\n")
    return listado


def mostrar_estudiante(listado):    
    suma = 0
    promedio = 0
    for valor in listado:
        suma += valor[2]
    promedio = suma / len(listado)
    
    print("\tEstudiantes con nota igual o mayor al promedio: ")
    for valor in listado:
        if valor[2] >= promedio:
            print(f"\nLegajo: {valor[0]}")
            print(f"Nombre: {valor[1]}")
            print(f"Nota: {valor[2]}")

def insertar_estudiante(listado):
    legajo  = int(input("\nIngrese legajo: "))
    nombre = input("Ingrese nombre: ")
    nota = int(input("Ingrese nota: "))
    lista = [legajo, nombre, nota] #esta lista siempre se actualiza
    listado.insert(0, lista)

#ORIGNAL
listado = registro()
mostrar_estudiante(listado)

print()
for clave, valor in enumerate(listado):
    print(clave, valor)
    
insertar_estudiante(listado)

print()
for clave, valor in enumerate(listado):
    print(clave, valor)

#ESTA FORMA HICE EN EL PARCIAL
def eliminar_a(cod):
    nuevo = cod.split(" ")
    for indice, valor in enumerate(nuevo):
        if valor.startswith("A") or valor.startswith("a"):
            del nuevo[indice]
            
    return " ".join(nuevo)

#ORIGINAL
cod = input("Ingrese una frase: ")
nueva_frase = eliminar_a(cod)
print("La nueva frase es: {}".format(nueva_frase))

#FORMA CORRECTA
def eliminar_a(cod):
    nuevo = cod.split(" ")
    resultado = []
    
    for valor in nuevo:
        if not valor.startswith("A") and not valor.startswith("a"):
            resultado.append(valor)
    
    return " ".join(resultado)

#ORIGINAL
cod = input("Ingrese una frase: ")
nueva_frase = eliminar_a(cod)
print("La nueva frase es: {}".format(nueva_frase))
