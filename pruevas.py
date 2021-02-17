import pandas as pd
import math
import numpy as nps


def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i][0]
    return sum/len(lista)


def varianza(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+math.pow((lista[i][0]-promediarLista(lista)),2)
    return sum/(len(lista))




xls=pd.ExcelFile('practica simulado real.xlsx')
print(xls.sheet_names)
df=xls.parse("Hoja1")
df1=xls.parse("Hoja2")
re=[]
re=df.values.tolist()
si=[]
si=df1.values.tolist()

print("reales ")
mere=promediarLista(re)
vame=varianza(re)
print(mere,vame)
print ("simulados")
mesi=promediarLista(si)
vasi=varianza(si)
print(mesi,vasi)

tdetabla=1.671
T=(mesi-mere)/(math.sqrt(vame/len(re)))
print(T,len(re))


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
if(abs(T)>2.000):
    print("se rechaza la hipotesis nula y se acepta la hipotesis alterna ")
else:
    print("se acepta  la hipotesis nula y se rechaza la hipotesis alterna ")