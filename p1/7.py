import math 
import random


def a(n):
    dato=[]
    f=[0.15,0.15,0.15,0.25,0.25,0.05]
    x=[1,2,3,4,5,6]
    
    for i in range(n):
        sum=0
        n=0
        r=random.random()
        while sum<r:
            sum=sum+f[n]
            n+=1
        
        dato.append(x[n-1])     
    return dato
def posion(lam,horas):
    datos=[]

    for j in range(horas):
        r=random.random()
        i=0
        sum=0
        while sum<r:
            sum=sum+math.exp(-lam)*math.pow(lam,i)/math.factorial(i)
            i=i+1
        datos.append(i)
 
    return(datos)  

def suma(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum


print(a(100))
l=posion(50,50)
print(l)
print("----------------------------")
print("min","catida de taras "," total tardado"," minuto que sale ")
minin=0
for i in range(len(l)):
    aux=a(l[i])
    sumas=suma(aux)
    minin=minin+round(sumas/60)
    print(i+1,"      ",l[i],"          ",round(sumas/60),"                  ",minin)

