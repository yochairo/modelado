import math 
import random

def uniforme(a,b):
    dato=[]
    for i in range(1000):
        r=random.random()
        res=a+r*(b-a)
        dato.append(res)
  
    return dato

def expo(lan):
    dato=[]
    for i in range(1000):
        r=random.random()
        res=-lan*math.log(1-r)
        dato.append(res)
   
    return dato

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)


lan=[100,124,50,123,80,75,55,60,70]
print(promediarLista(uniforme(45,121)))
a=promediarLista(lan)
print(promediarLista(expo(a)))
