import pandas as pd
import math
import numpy as np

def hmedia(lista):
    sum=0.0
    suf=0.0
    for i in range(0,len(lista)):
        sum=sum+i*lista[i]
        suf=suf+lista[i]
     
    return sum/suf

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
    return sum/(len(lista))


def frecacu(lista,k):
    dataacu=[]
    for i in range(0,len(lista)):
        sum=lista[i]/k
        dataacu.append(sum)
    return dataacu

def normal(inf,sup,media,var):
    sum=inf
    res=0.000
    while(sum<sup):
        l=-((sum-me)**2)/(2*va)
        
        res=res+(1/math.sqrt(2*math.pi*var))*math.exp(l)
        sum=sum+1
    return res



xls=pd.ExcelFile('practicadeaulaK-S.xlsx')
print(xls.sheet_names)
df=xls.parse()

lf=[]
lf=df.values.tolist()


print (len(lf))

n=math.sqrt(len(lf))
print(n)
sumar=20
aux1=20
rangos=[]
while (sumar<485):
    sumar=sumar+11
    aux=[aux1,sumar]
    aux1=sumar
    rangos.append(aux)
    

print(rangos)
print(len(rangos))

va=varianza(lf)
print("variaza",va)
me=promediarLista(lf)
print("media",me)
#print(promediarLista(lf))

frec=[]
for p in range(len(rangos)):
    a=rangos[p]
    sum=0
    for k in range(len(lf)):
        if(lf[k][0]>=a[0] and lf[k][0]<a[1]):
            sum+=1
    
    frec.append(sum)


#print(frec)
acu=acumulado(frec)
acf=frecacu(acu,len(lf))
fecpor=frecacu(frec,len(lf))

#print(acf)
#print(fecpor)


es=[]
for l in range(len(rangos)):
    a=rangos[l]
    au=normal(a[0],a[1],me,va)
    es.append(au)

print(es)

esacu=acumulado(es)
#print(acumulado(es))



for i in range(len(rangos)):
    print(rangos[i],"      ",acu[i],"          ",acf[i],"         ",es[i],"          ",esacu[i],"                  ")




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