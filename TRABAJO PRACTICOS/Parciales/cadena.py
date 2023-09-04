import os
os.system('cls')

def eliminar(cadena):
    cad='hola'
    c=list(cadena)
    print(c)
    del c[:5]
    print (c)
    frase = " ".join(c)
    print(frase)
  

#principal
cadena='hola mundo'
print(len(cadena))
eliminar(cadena)
