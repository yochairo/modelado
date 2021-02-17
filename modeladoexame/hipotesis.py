import pandas as pd
import math
import numpy as nps
import random


def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)


def varianza(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+math.pow((lista[i]-promediarLista(lista)),2)
    return sum/(len(lista))


def possion(media,l):
    lis=[]
    for j in range(l):
        lam=media
        r=random.random()
        i=0
        sum=0
        while sum<r:
            sum=sum+math.exp(-lam)*math.pow(lam,i)/math.factorial(i)
            i=i+1
        lis.append(i)
    
    return lis


print("reales ")
re=[14, 10, 12, 13, 11, 11, 9, 14, 10, 13, 11, 7, 16, 5, 19, 17, 10, 4, 8, 13, 12, 16, 14, 18, 11, 7, 9]
mere=promediarLista(re)
vame=varianza(re)
print(mere,vame)
print ("simulados")
si=possion(mere,len(re))
mesi=promediarLista(si)
vasi=varianza(si)
print(mesi,vasi)

tdetabla=1.7033  
T=(mesi-mere)/(math.sqrt(vame/len(re)))
print(T)


print("hipotesis nula : media de datos reales = media de datos simulados")
print("hipotesis alterna : media de datos reales > media de datos simulados")
print("cola derecaha")
if(T>tdetabla):
    print("se rechaza la hipotesis nula y se acepta la hipotesis alterna ")
else:
    print("se acepta  la hipotesis nula y se rechaza la hipotesis alterna ")
print("cola izquierda")
if(T<-tdetabla):
    print("se rechaza la hipotesis nula y se acepta la hipotesis alterna ")
else:
    print("se acepta  la hipotesis nula y se rechaza la hipotesis alterna ")

print("dos cola")
if(abs(T)>2.0518):
    print("se rechaza la hipotesis nula y se acepta la hipotesis alterna ")
else:
    print("se acepta  la hipotesis nula y se rechaza la hipotesis alterna ")