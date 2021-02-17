import math 
import random 
import numpy as np

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)

def espe(nl):
    datos=[]
    
    for l in range(nl) :
        aux=[]
        al=[]
        for j in range(100):
            n=1
            mul=1
            a=True
            while (a):
                u=random.random()
               # print(u)
                al.append(u)
                mul=mul*u
                n+=1
                if(mul<math.exp(-3)):
                    a=False
            aux.append(n)

        print(aux)
        print(promediarLista(al))    
        a=np.amax(aux)
        datos.append(a)
    
    
    print(promediarLista(datos))
    ##print(datos)
   

espe(100)
##espe(1000)
##espe(10000)