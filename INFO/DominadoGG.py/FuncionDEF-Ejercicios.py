"""Operaciones básicas en python (+-*/) con menu de opciones utilizando funciones"""

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b

#ORIGINAL
while True:
    print("****Menu de opciones****") #\n: SIRVE PARA HACER SALTO DE LINEA
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion = input("Ingrese la opción que desea realizar: ")
    nro1 = float(input("Ingreseo nro1: "))
    nro2 = float(input("Ingreseo nro2: "))
    
    if opcion == "1":
        print("La suma es: ",suma(nro1,nro2))
    elif opcion == "2":
        print("La rseta es: ",resta(nro1, nro2))
    elif opcion == "3":
        print("La multiplicacion es: ",multiplicacion(nro1, nro2))
    elif opcion == "4":
        print("La division es: ",division(nro1,nro2))
    else:
        print("Opción inválida")
        
#PARA RECIBIR MULTIPLES ARGUMENTOS USANDO UN SOLO PARAMETRO
def verificar(*notas):
    aprobadas = 0
    desaprobadas = 0
    for nota in notas:
        if nota > 5:
            aprobadas += 1
        else:
            desaprobadas += 1
    return f"{aprobadas} materias aprobadas, {desaprobadas} materias desaprobadas"

while True:
    analisis_mat = int(input("Ingrese su nota de Análisis Matemático: "))
    algebra = int(input("Ingrese su nota de Álgebra: "))
    programacion = int(input("Ingrese su nota de programación: "))
    ingles = int(input("Ingrese su nota de inglés: "))
    
    resultado = verificar(analisis_mat, algebra, programacion, ingles) 
    print(resultado)
    
#OTRA FORMA | POR SI ACASO XD: EL ASTERISCO se denomina "operador de desempaquetado" o "operador de expansión"
def concatenar_cadenas(*cadenas):
    resultado = ""
    for cadena in cadenas:
        resultado += cadena
    return resultado

texto = concatenar_cadenas("Hola", " ", "Mundo", "!")

print(texto)  # Output: "Hola Mundo!"
#OTRA FORMA
    
#OTRA FORMA | PASANDO ARGUMENTOS INDIVUDUALMENTE PERO USANDO 1 SOLO PARAMETRO
def verificar(nota):
    if nota > 50:
        return "usted está aprobado"
    else:
        return "usted está desaprobado"

while True:
    resultado = 0
    analisis_mat = int(input("Ingrese su nota de Análisis Matemático: "))
    algebra = int(input("Ingrese su nota de Álgebra: "))
    programacion = int(input("Ingrese su nota de programación: "))
    ingles = int(input("Ingrese su nota de inglés: "))
    
    print(f"Nota de Análisis Matemático: {analisis_mat} - {verificar(analisis_mat)}")
    print(f"Nota de Álgebra: {algebra} - {verificar(algebra)}")
    print(f"Nota de programación: {programacion} - {verificar(programacion)}")
    print(f"Nota de inglés: {ingles} - {verificar(ingles)}")
    
#DE UNA LISTA DE NUMEROS
def calcular_promedio(*numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

resultado = calcular_promedio(10, 20, 30, 40, 50)
print(resultado)  # Output: 30.0