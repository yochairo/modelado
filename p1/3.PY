import math 
import random 
import numpy as np


def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)

def hay5(lista):
    sum=0.0
    for i in range(0,len(lista)):
        if(lista[i]==5):
            sum+=1
            print(i)
    return sum


datos=[]
suma=[]
for l in range(50000) :
    aux=[]
    sum=0
    for i in range(5):
        r=random.randint(1,6)
        aux.append(r)
        sum=sum+r
    #print(aux,sum)
    suma.append(sum)
    datos.append(aux)
print(suma)
print(promediarLista(suma))





