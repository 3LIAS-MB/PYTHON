#EJERCICIO 6
""" Diseñar un programa que, mediante un menú de opciones, permite realizar lo siguiente:
a. Cargar dos listas (lista01 y lista02) de contactos de una agenda digital, donde cada contacto tiene
número de celular, nombre y correo electrónico.
b. Mostrar las listas generadas
c. Generar la lista03 que contenga la fusión de las dos primeras, considerar lo siguiente:
i. Pueden existir contactos que tengan el mismo número de celular en lista01 y lista02
ii. Lista03 puede generarse agregando primero lista01 y luego lista02, pero debe validar que el
número de celular no se haya agregado previamente. De ser así debe mostrar un mensaje
informando que ya existe el contacto y pedir al usuario que elija cuál de los dos contactos
corresponde que se guarde en lista03.
d. Salir"""

def menu():
    while True:
        print("\t-MENU-")
        print("a. Cargar listas (lista01 y lista02)")
        print("b. Mostrar las listas generadas")
        print("c. Generar lista 03")
        print("d. Salir")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "a":
            cargar_listas()
        elif opcion == "b":
            mostrar_listas()
        elif opcion == "c":
            generar_lista03()
        elif opcion == "d":
            print("\nGracias por usar nuestro programa. ¡Hasta luego!")
            break
            
def cargar_listas():
    cargar1 = int(input("¿Cuantos contactos quiere cargar a la lista01?: "))
    cargar2 = int(input("¿Cuantos contactos quiere cargar a la lista02?: "))

    if cargar1 >= 0 and cargar2 >= 0:
        for _ in range(cargar1):
            nombre = input("\nIngrese nombre: ")
            celular = input("Ingrese numero de celular: ")
            correo = input("Ingrese correo electronico: ")
            lista01.append({'nombre': nombre, 'celular': celular, 'correo': correo})
            
        for _ in range(cargar2):
            nombre = input("\nIngrese nombre: ")
            celular = input("Ingrese numero de celular: ")
            correo = input("Ingrese correo electronico: ")
            lista02.append({'nombre': nombre, 'celular': celular, 'correo': correo})
        print("\nListas cargadas exitosamente!\n")
    else:
        print("\nError: No pueden ser numeros negativos")
    
def mostrar_listas():
    if len(lista01) > 0:
        print("\nLista 01:")
        for lst1 in lista01:
            print(f"\nNombre: {lst1['nombre']}")
            print(f"Celular: {lst1['celular']}")
            print(f"Correo: {lst1['correo']}")
    else:
        print("\nError: No hay contactos en la lista01")
        
    if len(lista02) > 0:
        print("\nLista 02:")
        for lst2 in lista02:
            print(f"\nNombre: {lst2['nombre']}")
            print(f"Celular: {lst2['celular']}")
            print(f"Correo: {lst2['correo']}")
        print()
    else:
        print("\nError: No hay contactos en la lista02\n")

def generar_lista03():
    
    lista03 = lista01.copy() #una forma mas facil de agregar todos los elementos a la lista03
    
    # for lst1 in lista01:
    #     lista03.append(lst1)
    
    for lst2 in lista02:
        for lst3 in lista03:
            if lst2['celular'] == lst3['celular']:
                elegir = input(f"El numero {lst2['celular']} esta repetido. ¿Cual contacto desea conservar: 1. list01 o 2. list01?: ")
                if elegir == "1":
                    continue
                
                elif elegir == "2":
                    lst3['celular'] = lst2['celular']
                    
# def generar_lista03(lista01, lista02, lista03):
#     print("\n-- Generar Lista03 --")
    
#     lista03 = lista01.copy()
    
#     for contacto in lista02:
#         celular = contacto["celular"] #Para cada numero de celular de lista02 se guarda en "celular"
#         if celular in [c["celular"] for c in lista03]: #Se realiza una verificación para determinar si el celular ya existe en lista03
#             print(f"Ya existe un contacto con el número de celular {celular}")
#             opcion = input("¿Cuál de los dos contactos desea conservar? (1 - lista01, 2 - lista02): ")
#             if opcion == "1": #Si el usuario eleje "1" se ejecuta "continue" para pasar el siguiente contacto (se conserva el contacto existente)
#                 continue 
#             elif opcion == "2":
#                 lista03 = [c for c in lista03 if c["celular"] != celular] #se actualiza lista03 para eliminar los contactos duplicados, o sea elimina lo de lista01
#         lista03.append(contacto) #se le agrega "contacto" que seria un diccionario de lista02
        
    if len(lista03) > 0:
        print("\nLista generada:")
        for lst3 in lista03:
            print(f"\nNombre: {lst3['nombre']}")
            print(f"Celular: {lst3['celular']}")
            print(f"Correo: {lst3['correo']}")
        print()
                    
    
#ORIGINAL
lista01 = list()
lista02 = list()
lista03 = list()
menu()