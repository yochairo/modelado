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

def bino(media,l,n):
    lis=[]
    p = media/n
    q=1-p
    for j in range(l):
        r=random.random()
        i=0
        sum=0
        while sum<r:
            b=math.pow(p,i)*math.pow(q,n-i)
            sum=sum+math.factorial(n)/(math.factorial(i)*math.factorial(n-i))*b
            i=i+1
        lis.append(i)
    
    return lis


print("reales ")
re=[5,	3,	4,
3,	3,	1,
2,	3,	5,
2,	2,	3,
3,	2,	4,
2,	2,	4,
2,	6,	3,
2,	5,	3,
3,	2,	3,
3,	3,	3,
3,	10,	4,
9,	4,	4,
4,	2,	1,
4,	2,	3,
3,	1,	2,
1,	2,	3,
3,	4,	3,
3,	3,	2,
3,	3,	3,
5,	3,	2,
5,	5,	3,
2,	3,	3,
1,	4,	4,
4,	3,	3,
4,	2,	2,
2,	3,	1,
2,	3,	5,
3,	1,	2,
4,	2,	1,
2,	1,	1]
mere=promediarLista(re)
vame=varianza(re)
print(mere,vame)
print ("simulados")
si=bino(mere,len(re),max(re))
mesi=promediarLista(si)
vasi=varianza(si)
print(mesi,vasi)

tdetabla=1.6622 
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
if(abs(T)>1.9870):
    print("se rechaza la hipotesis nula y se acepta la hipotesis alterna ")
else:
    print("se acepta  la hipotesis nula y se rechaza la hipotesis alterna ")