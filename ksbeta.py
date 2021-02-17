import pandas as pd
import math
import numpy as np

def lsn(lista):
    sum=0.0
    l=[]
    for i in range(0,len(lista)):
        a=lista[i]
        print(a)
        l.append(a)
    #print(l)
    return l

def acumulado(lista):
    dataacu=[]
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
        dataacu.append(sum)
    return dataacu
    
def minimo(lista):
    max=lista[0]
    for i in range(1,len(lista)):
        if(max<lista[i]):
            max=lista[i]
    return min

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i][0]
    return sum/len(lista)


def varianza(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+math.pow((lista[i][0]-promediarLista(lista)),2)
    return sum/(len(lista)-1)


def frecacu(lista,k):
    dataacu=[]
    for i in range(0,len(lista)):
        sum=lista[i]/k
        dataacu.append(sum)
    return dataacu

def gmamafun(z):
    m=1
    for l in range(1,1000):
        m=m*(math.pow((1+1/l),z))/(1+z/l)
    return (1/z)*m

def funbeta(inf,sup,a,b):
    sum=inf
    res=0.000
    while(sum<sup):
        al=math.gamma(a+b)/(math.gamma(a)+math.gamma(b))
        res=res+al*math.pow(sum,a-1)*math.pow(1-sum,b-1)
        sum=sum+1
    return res


xls=pd.ExcelFile('practicadeaulaK-S.xlsx')
print(xls.sheet_names)
df=xls.parse()

lf=[]
lf=df.values.tolist()


print (len(lf))

n=math.sqrt(len(lf))

sumar=20
aux1=20
rangos=[]
while (sumar<485):
    sumar=sumar+11
    aux=[aux1,sumar]
    aux1=sumar
    rangos.append(aux)


##rangos sonlos intervalos 
va=varianza(lf)
print("variaza",va)
me=promediarLista(lf)
print("media",me)

frec=[]
for p in range(len(rangos)):
    a=rangos[p]
    sum=0
    for k in range(len(lf)):
        if(lf[k][0]>=a[0] and lf[k][0]<a[1]):
            sum+=1
    
    frec.append(sum)


#print(frec)
#inprime las frecuensias en numero #
acu=acumulado(frec)
acf=frecacu(acu,len(lf))
fecpor=frecacu(frec,len(lf))

#print(acf)#acumulado en porcentaje
#print(fecpor)#frec en procentaje


es=[]
alfa=(1-me/va)*(me**2)-me
beta=((1-me)/me)*alfa
print(alfa,beta)
for l in range(len(rangos)):
    a=rangos[l]
    au=funbeta(a[0],a[1],alfa,beta)
    es.append(au)

print(es)

esacu=acumulado(es)
#print(acumulado(es))



#for i in range(len(rangos)):
#    print(rangos[i],"      ",acu[i],"          ",acf[i],"         ",es[i],"          ",esacu[i],"                  ")




dmax=[]
for f in range(len(rangos)):
    aux=acf[f]-esacu[f]
    dmax.append(abs(aux))
#print(dmax)
dmaxi=max(dmax)



dta=0.733/math.sqrt(len(lf))
print(dta)
if(dmaxi>dta):
    print("son diferentes")
else :
    print("se rechazan")