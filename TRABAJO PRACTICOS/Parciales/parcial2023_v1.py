import os
os.system ('cls')

def cargar(A,B,C,D):
    for i in range (len(A)):
       nombre=A[i]
       nota= B[i]
       legajo=C[i]

       D.append([nombre,nota,legajo])
    return D   

def mostrar (D):
    for i in range (len(D)) :
        print(D[i])

def promedio(D):
    suma=0
    for i in range(len(D)):
        suma+=D[i][1] # sumo las notas
    p=suma/len(D)    
    print('promedio:',p)
    for i in range (len(D)):
        if D[i][1]>=p:
            print(D[i][0])

def inicio(D):
    nombre=input('name:')
    nota=float(input('nota:'))
    legajo=int(input('legajo:'))
    D.insert(0,[nombre,nota,legajo])

    return D

#Principal
A=['maria','Nicole', 'pedro']
B=[10,8.9,100]
C=[2593,2587,9854]

D=[]

D=cargar(A,B,C,D)
mostrar(D)
promedio(D)
inicio(D)
print(D)