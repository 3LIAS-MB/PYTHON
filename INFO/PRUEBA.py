#CASOS DE ESTUDIO
"""Mediante un menú de opciones realizar el siguiente programa modular para gestionar el listado de notas de un
examen para los estudiantes de una institución educativa:

1. Registrar estudiantes: para cada uno se debe solicitar DNI, nombre y nota. Validar que la nota se
encuentre entre 0 y 10. El proceso finaliza cuando se ingresa un DNI igual a cero.
2. Mostrar el listado de estudiantes con sus respectivas notas.
3. Buscar a un estudiante por su DNI y mostrar su nombre y nota.
4. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).
5. Eliminar a un estudiante por su DNI. Emitir un mensaje de confirmación.
6. Mostrar los estudiantes que obtuvieron nota mayor o igual a una dada y el promedio correspondiente"""

def menu():
    estudiantes = dict()
    while True:
        print()
        print("\t-MENU-")
        print("1. Registrar estudiantes")   
        print("2. Mostrar listado")
        print("3. Buscar estudiante por su DNI")
        print("4. Modificar los datos de un estudiante")
        print("5. Eliminar a un estudiante por su DNI")
        print("6. Mostrar estudiantes con mayor nota y el promedio")
        print("7. Salir")
        opcion = input("\nIngrese una opcion [1, 7]: ")
        if opcion == "1":
            registrar_estudiantes(estudiantes)
        elif opcion == "2":
            mostrar_listado(estudiantes)
        elif opcion == "3":
            buscar_estudiante(estudiantes)
        elif opcion == "4":
            modificar_datos(estudiantes)
        elif opcion == "5":
            eliminar_estudiante(estudiantes)
        elif opcion == "6":
            mayor_alpromedio(estudiantes)
        elif opcion == "7":
            print("\nGracias por usar nuestro programa!")
            break
        else:
            print("Error, opcion invalida. Intente nuevamente")
            
def registrar_estudiantes(estudiantes):
    while True:
        dni = int(input("\nIngrese su DNI (0 para salir): "))
        if dni == 0:
            break
        if dni in estudiantes:
            print("Error: El estudiante ya está registrado.")
            continue #-> ignora el resto del codigo y vuelve al inicio del bucle
        nombre = input("Ingrese su nombre: ")
        nota = int(input("Ingrese su nota: "))
        while nota < 0 or nota > 10:
            print("Error: nota fuera de rango [0, 10]")
            nota = int(input("Ingrese su nota: "))
        estudiantes[dni] = {"nombre": nombre, "nota": nota}
        
def mostrar_listado(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for clave, valor in estudiantes.items():
            print(f'DNI: {clave}')
            print(f'Nombre: {valor["nombre"]}')
            print(f'Nota: {valor["nota"]}')
            print()

def buscar_estudiante(estudiantes):
    dni = int(input("Ingrese el DNI del estudiante para buscarlo: "))
    if dni in estudiantes: #-> dni solo recorre las claves, es decir, el dni
        estudiante = estudiantes[dni] #-> "estudiante" toma los elementos del diccionario, pero no la clave
        print("\nEstudiante encontrado:")
        print(f'\nNombre: {estudiante["nombre"]}')
        print(f'Nota: {estudiante["nota"]}')
    else:
        print("Estudiante no encontrado.")
            
def modificar_datos(estudiantes):
    dni = int(input("Ingrese el DNI del estudiante para modificarlo: "))
    if dni in estudiantes:
        estudiante = estudiantes[dni]
        nombre = input("Ingrese nombre nuevo: ")
        nota = int(input("Ingrese nota nueva: "))
        while nota < 0 or nota > 10:
            print("Error: nota fuera de rango [0, 10]")
            nota = int(input("Ingrese nota nueva: "))
        estudiante["nombre"] = nombre
        estudiante["nota"] = nota
        print("\nEstudiante modificado con éxito!")
    else:
        print("Estudiante no encontrado.")

def eliminar_estudiante(estudiantes):
    dni = int(input("Ingrese el DNI del estudiante para eliminarlo: "))
    for clave in estudiantes.keys():
        if clave == dni:
            del estudiantes[clave]
            break
    print("\nEstudiante eliminado  con exito!")

# def eliminar_estudiante(estudiantes):
#     dni = int(input("Ingrese el DNI del estudiante para eliminarlo: "))
#     if dni in estudiantes:
#         del estudiantes[dni]
#         print("\nEstudiante eliminado con éxito!")
#     else:
#         print("Estudiante no encontrado.")
        
def mayor_alpromedio(estudiantes):
    nota_dada = int(input("Ingrese una nota limite: "))
    suma = 0
    cantidad = 0
    for clave, valor in estudiantes.items():
        if valor["nota"] >= nota_dada:
            print(f'\nDNI: {clave}')
            print(f'Nombre: {valor["nombre"]}')
            print(f'Nota: {valor["nota"]}')
            suma += valor["nota"]
            cantidad += 1

    if cantidad == 0:
        print("No hay estudiantes con una nota mayor o igual a la nota límite.")
    else:
        promedio = suma / cantidad
        print(f'El promedio general es de {promedio}')

        
#ORIGINAL
menu()
