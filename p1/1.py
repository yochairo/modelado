import math 
import random 
import numpy as np

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)
def minimo(lista):
    min=lista[0]
    for i in range(1,len(lista)):
        if(min>lista[i]):
            min=lista[i]
    return min

def espe(nl):
    datos=[]
    for l in range(nl) :
        aux=[]
        for j in range(5):
            n=1
            sum=0
            while (sum<=1) :
                u=random.random()
                sum=sum+u
                n+=1
            aux.append(n)
        ##print(aux)    
        a=minimo(aux)
        datos.append(a)
    
    
    print(promediarLista(datos))
    ##print(datos)

espe(100)
espe(1000)
espe(10000)

