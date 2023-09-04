#------------CONDICIONALES (if, elif, else)-------------

ingreso_mensual = 81000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en defecit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien pa")
    else:
        print("estas gastando una banda, para un poco")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en argentina")
elif ingreso_mensual > 200:
    print("estas bien en venezuela")