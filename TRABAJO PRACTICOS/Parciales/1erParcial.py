#PUNTO 1
"""En una tienda venden dos tipos de articulos, de equiqueta amarilla y de etiqueta verde ambos tipos de articulos
tienen el precio unitario. Cada cliente puede comprar un solo tipo de articulo (amarillo o verde) para ello debe
indicar la cantidad a comprar. Los clientes se identifican por un numero correlativo automatico. Los articulos
que tengan etiqueta verde tienen un descuento del 20% si se compran en cantidades inferiores a 10. Se debe saber
cuanto debe pagar cada cliente. Al final de la jornada se quiere saber:
- Cuantos articulos de tipo amarillo se vendieron
- El cliente que gasto mas dinero

Validar las entradas: el precio unitario es mayor a 100 y menor a 200. Las cantidades deben ser mayores a cero.
Utilice modulos para las validaciones."""

def validar_precioU(precio):
        return precio > 100 and precio < 200

def validar_cantidades(cantidad):
    return cantidad > 0

#ORIGINAL
cliente = 0
amarillo = 0
cliente_max = 0
total = 0
lol = 0
iniciar_dia = input("¿Quiere iniciar el día laboral? si/no: ")
precio = int(input("Ingrese el precio de su producto para iniciar el día: "))
validar_precioU(precio)
while iniciar_dia == "si":      
    print()
    print("¿Qué tipo de articulo desea comprar? \n 1. Etiqueta amarilla \n 2. Etiqueta verde")
    print()
    etiqueta = int(input("Escoje una opción: "))
    cantidad = int(input("Ingrese la cantidad: "))
    validar_cantidades(cantidad)
    if validar_cantidades and validar_precioU:
        totalt2 =  precio * cantidad
        cliente += 1
        if etiqueta == 2:
                total  = totalt2 * (1 - 0.2)
        elif etiqueta == 1:
            amarillo += 1
            total = totalt2
        if total > lol:
            lol = total
            cliente_max = cliente
            
            print("Usted debe pagar: ",total)
            print()
        iniciar_dia = input("¿Continuar? si/no: ")
print(f"Se vendieron {amarillo} articulos de tipo amarillo")
print(f"El cliente {cliente_max} gastó más dinero que todos ")
print()
print("GRACIAS POR ELEJIRNOS!")

#PUNTO 2-a)

nro = int(input("nro: "))
flag = not nro != 0 and nro <= 10
suma = 0
for i in range(1, nro, 3):
    if flag:
        suma += i
    else:
        suma += nro
    flag = not flag
print(suma)

#PUNTO 2-b) ->>>> analizar

def f2(v, w=9):
    z = w - v + 2
    return z

def f1(p=2, q=5):
    r = p + f2(q)
    return r

nro1 = int(input("nro1: "))
nro2 = int(input("nro2: "))
print(f1(nro1,nro2))

#PUNTO A
"""Hacer un algoritmo en python para procesar los datos de encomienda. Por cada encomienda, se 
ingresan los siguientes datos: N° de encomienda, peso y tipo. El peso debe ser mayor 
o igual a cero y menor o igual a los 10kg y el tipo puede ser simple (S) o certificado 
(C). Se debe calcular y mostrar el monto a pagar por cada encomienda, teniendo en 
cuenta lo siguiente: 
El precio básico de la encomienda simple es $50 y para la certificada es $200, según 
el peso se realizan los siguientes recargos al precio: recargo del 10% si el peso es 
mayor o igual a 1kg y menor a 2kg, recargo del 20% si el peso es mayor o igual a 2 kg 
y menor a 5kg y el recargo del 50%, si el peso es mayor o igual a 5kg.
El proceso finaliza cuando se ingresa un número de encomienda igual a 0. Se desea 
informar también, el peso total y la cantidad de encomiendas simples y certificadas."""

nro_encomienda = int(input("Ingresar número de encomienda (0 para salir): "))
contador_s = 0
contador_c = 0  
total_peso = 0

while nro_encomienda != 0:
    peso = int(input("Ingresar peso: "))
    if peso >= 0 and peso <= 10:
        tipo = input("Ingresar tipo de encomienda: simple (s) o certificada (c): ")
        
        if tipo == "s":
            precio = 50
            contador_s += 1
        else:
            precio = 200
            contador_c += 1
            
        if peso >= 1 and peso < 2:
            recargo = precio * (0.1 + 1)
        elif peso >= 2 and peso < 5:
            recargo = precio * (0.2 +1)
        elif peso >= 5:
            recargo = precio * (0.5 + 1)
        total_peso += peso
        
        print("El monto a pagar es de: ",recargo)
        nro_encomienda = int(input("Ingresar número de encomienda (0 para salir): "))
    else:
        print("Peso invalido")
        break  
print("La cantidad de encomiendas simples que se realizaron son de: ",contador_s)
print("La cantidad de encomiendas certificadas que se realizaron son de: ",contador_c)
print("El peso total es de: ",total_peso)

#FORMA 2, LA DEJO PORQUE ME PARECE INTERESANTE LA LINEA 63 (CHATGPT)

# inicializar variables
peso_total = 0
cant_simple = 0
cant_certif = 0

# procesar encomiendas
while True:
    num_encomienda = int(input("Ingrese el número de encomienda (0 para finalizar): "))
    if num_encomienda == 0:
        break
    peso = float(input("Ingrese el peso de la encomienda (en kg): "))
    tipo = input("Ingrese el tipo de encomienda (S para simple, C para certificada): ")
    precio_base = 50 if tipo == "S" else 200
    recargo = 0.1 if peso >= 1 and peso < 2 else 0.2 if peso >= 2 and peso < 5 else 0.5 if peso >= 5 else 0
    monto = precio_base * (1 + recargo)
    peso_total += peso
    if tipo == "S":
        cant_simple += 1
    elif tipo == "C":
        cant_certif += 1
    print(f"Monto a pagar por la encomienda {num_encomienda}: ${monto}")

# mostrar resultados finales 
print(f"Peso total de las encomiendas: {peso_total} kg")
print(f"Cantidad de encomiendas simples: {cant_simple}")
print(f"Cantidad de encomiendas certificadas: {cant_certif}")

#PUNTO B
"""Hacer un algoritmo para procesar la venta de artículos de un minimercado. En el lapso 
de una jornada un cliente solo compra un tipo de artículo. Para cada cliente el 
empleado del mini mercado ingresa: tipo de artículo y la cantidad. Si el tipo es 3, el precio es $30,00;
si el tipo es 5 el precio es  $50,00; si la cantidad que se vende de un artículo es mayor o igual a 5 y
menor o igual a 10 se hace un descuento del 20%, si la cantidad es mayor a 10 el descuento es del  50%.

Se desea calcular y mostrar el monto que debe pagar cada cliente y al finalizar la 
jornada se desea conocer cuántos artículos de los diferentes tipos que se vendieron. """

cantidad = int(input("Ingreasar cantidad de articulos (ingresar 0 para salir): "))
tipo_3 = 0
tipo_5 = 0

while cantidad != 0:
    tipo = int(input("Ingresar tipo de articulo (3 o 5): "))
    
    if tipo == 3:
        precio = 30
        tipo_3 += 1 
    elif tipo == 5:
        precio = 50
        tipo_5 += 1
        
    if cantidad >= 5 and cantidad <= 10:
        total = precio * cantidad
        descuento = total * 0.2
        descuento_total = total - descuento
    elif cantidad > 10:
        total = precio * cantidad
        descuento = total * 0.5
        descuento_total = total - descuento
    else:
        descuento_total = precio * cantidad
        
    print("Debe pagar: ",descuento_total)
    cantidad = int(input("Ingreasar cantidad de articulos (ingresar 0 para salir): "))
print(f"Se vendieron {tipo_3} articulos del tipo 3 y {tipo_5} del tipo 5")

#PUNTO C
"""Una empresa de colectivos vende 100 pasajes para un viaje a Tucumán, el precio del 
pasaje es de 900.00 pesos, se pueden pagar a contado o con tarjeta. Si paga al 
contado, el precio tiene un descuento del 10% y con tarjeta el precio aumenta 15%. El 
precio del pasaje también puede tener un descuento adicional de 25% si es jubilado. 
Se solicita a cada pasajero si va a pagar al contado o con tarjeta, y si es jubilado o no. 
Se debe controlar que haya pasajes disponibles para vender y el precio que paga cada 
pasajero y al finalizar cuál es el monto total recaudado por la empresa. El algoritmo 
termina cuando no hay más pasajes para vender."""

pasajes = 100
precio = 900
monto_total = 0
descuento_total = 0

while pasajes != 0:
    formaDePago = input("Ingresar forma de pago, al contado (c) o tarjeta (t): ")
    jubilado = input("Es usted jubilado? s/n: ")
    
    if formaDePago == "c":
        descuento = precio * 0.1
        if jubilado == "s":
            descuento += precio * 0.25
        descuento_total = precio - descuento
            
    elif formaDePago == "t":
        aumento = precio * 0.15
        if jubilado == "s":
            aumento = aumento - precio * 0.25
        descuento_total = precio + aumento
        
    pasajes -= 1
    monto_total += descuento_total
    
    print("Precio del pasaje: ",descuento_total)
    print("Pasajes disponibles: ",pasajes)
print("El monto total es: ",monto_total)

#FORMA 2 PERO ELIGIENDO CUANTOS PASAJES QUIERO COMPRAR
pasajes = 100
precio = 900
monto_total = 0
descuento_total = 0

while pasajes != 0:
    formaDePago = input("Ingresar forma de pago, al contado (c) o tarjeta (t): ")
    jubilado = input("Es usted jubilado? s/n: ")
    comprar_pasajes = int(input("Cuantos pasajes desea comprar?: "))
    
    if formaDePago == "c":
        total = comprar_pasajes * precio
        descuento = total * 0.1
        if jubilado == "s":
            descuento += total * 0.25
        descuento_total = total - descuento
            
    elif formaDePago == "t":
        total = comprar_pasajes * precio
        aumento = total * 0.15
        if jubilado == "s":
            aumento = aumento - total * 0.25
        descuento_total = total + aumento
        
    pasajes -= comprar_pasajes 
    monto_total += descuento_total
    
    print("Precio del pasaje: ",descuento_total)
    print("Pasajes disponibles: ",pasajes)
print("El monto total es: ",monto_total)

#PUNTO D
"""La empresa Comodín tiene al inicio de la jornada un stock inicial de un tipo de 
mercadería, llegan camiones para llevarse la mercadería a las sucursales C o D, se 
debe controlar que exista cantidad suficiente para poder llevarse dicha mercadería, en 
caso de que no pueda llevarse, se debe mostrar un mensaje en el que se diga que 
esta faltando mercaderia. Se desea conocer el stock después de que cada camión se 
va. Al finalizar la jornada se desea saber la cantidad total de mercaderías de las 
distintas sucursales y cuántos camiones llevaron mercadería y se debe mostrar el 
stock que quedó al final en el Comodín."""


mercaderia = int(input("Ingrese la cantidad de mercaderia: "))
stock_actual = mercaderia
llevado = 0
sucursal_c = 0
sucursal_d = 0

while True:
    sucursal = input("A qué sucursal desea transportar mercaderia C/D?: ")
    llevar = int(input("Cuanta mercaderia desea llevar a esa sucursal?: "))
    
    if sucursal == "C":
        if llevar <= stock_actual:
            stock_actual -= llevar
            sucursal_c += llevar
    if sucursal == "D":
        if llevar <= stock_actual:
            stock_actual -= llevar
            sucursal_d += llevar
        else:
             print("Stock insuficiente de mercaderia")
    print("El stock actual es de: ",stock_actual)
    continuar = input("Desea continar? S/N: ")
    if continuar == "S":
        continue
    else: 
        break
print("El total de mercaderia de la sucursal C es de: ",sucursal_c)
print("El total de mercaderia de la sucursal D es de: ",sucursal_d)
print("Stock actual del Comodin: ",stock_actual)

#FORMA 2 CON CHATGPT
stock_inicial = int(input("Ingrese la cantidad de mercadería en stock al inicio del día: "))
stock_actual = stock_inicial
camiones = 0
cant_suc_c = 0
cant_suc_d = 0

while True:
    print("Stock actual: ", stock_actual)
    sucursal = input("A qué sucursal va el camión? (C/D): ")
    cant = int(input("Cuánta mercadería lleva el camión? "))
    
    if sucursal == "C":
        if cant <= stock_actual:
            stock_actual -= cant
            cant_suc_c += cant
            camiones += 1
        else:
            print("No hay suficiente mercadería en stock para enviar a la sucursal C.")
    elif sucursal == "D":
        if cant <= stock_actual:
            stock_actual -= cant
            cant_suc_d += cant
            camiones += 1
        else:
            print("No hay suficiente mercadería en stock para enviar a la sucursal D.")
    else:
        print("Sucursal inválida, ingrese C o D.")
    
    seguir = input("Desea continuar cargando camiones? (S/N): ")
    if seguir.upper() == "N":
        break

print("Total de camiones cargados:", camiones)
print("Cantidad total de mercadería enviada a la sucursal C:", cant_suc_c)
print("Cantidad total de mercadería enviada a la sucursal D:", cant_suc_d)
print("Stock final en el Comodín:", stock_actual)

#PUNTO E
"""La panadería “Buen Día” tiene que vender 1000 facturas, el precio de cada factura es 
de $5. Los clientes pueden pagar a contado ( C ), o Tarjeta (T). Si el cliente paga al 
contado se realiza un descuento del 10% si su compra es superior a $200. Si no supera 
dicha compra paga el precio normal (sin el descuento), si paga con tarjeta se le realiza 
un aumento del 15%. La panadería elaboró un programa para estimular sus ventas: a 
los clientes que lleven más de 50 facturas se les da un descuento de $25 al valor de 
su compra. Se debe mostrar el total a pagar por cada cliente. Al finalizar el día laboral 
se desea conocer cuántos clientes se atendieron, la cantidad de clientes que pagaron 
al contado y la cantidad de los que pagaron con tarjeta, también la cantidad de facturas 
que quedaron."""

facturas = 1000
precio = 5
total = 0
aumento = 0
clientes = 0
clientes_c = 0
clientes_t = 0

while facturas > 0:
    forma_de_pago = input("Ingrese su forma de pago CONTADO/TARJETA (C/T): ")
    cantidad = int(input("¿Cuantas facturas desea comprar?: "))
    
    total = precio * cantidad
    if cantidad > 50:
        total -=25
        
    if forma_de_pago == "C":
        if total > 200:
            total *= (1 - 0.1)
            clientes += 1
            clientes_c += 1 
    if forma_de_pago == "T":
        total *= (1 + 0.15)
        clientes += 1
        clientes_t += 1
    facturas -= cantidad

        
    print("Debe pagar: ",total)
print(f"En total se atendieron {clientes} clientes.")
print(f"{clientes_c} clientes pagaron al contado")
print(f"{clientes_t} clientes pagaron con tarjeta")
print("Quedaron",facturas,"facturas")

#FORMA 2 CON CHATGPT
facturas_vendidas = 0
precio_factura = 5
clientes_atendidos = 0
facturas_contado = 0
facturas_tarjeta = 0
facturas_restantes = 1000

while facturas_vendidas < 1000:
    forma_pago = input("¿Cómo desea pagar? Contado (C) o Tarjeta (T): ")
    cantidad_facturas = int(input("¿Cuántas facturas desea comprar? "))
    total = precio_factura * cantidad_facturas
    
    if cantidad_facturas > 50:
        total -= 25
    
    if forma_pago == "C":
        if total > 200:
            total *= 0.9
            facturas_contado += cantidad_facturas
        else:
            facturas_contado += cantidad_facturas
    elif forma_pago == "T":
        total *= 1.15
        facturas_tarjeta += cantidad_facturas
    
    print("El total a pagar es: $", total)
    
    facturas_vendidas += cantidad_facturas
    clientes_atendidos += 1
    facturas_restantes = 1000 - facturas_vendidas
    
print("Clientes atendidos:", clientes_atendidos)
print("Cantidad de facturas vendidas al contado:", facturas_contado)
print("Cantidad de facturas vendidas con tarjeta:", facturas_tarjeta)
print("Facturas restantes:", facturas_restantes)