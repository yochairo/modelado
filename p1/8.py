import math 
import random
import matplotlib.pyplot as plt

def uniforme(a,b,rango):
    dato=[]
    for i in range(rango):
        r=random.random()
        res=a+r*(b-a)
        dato.append(res)
  
    return dato

def uniformereparo(a,b):
    r=random.random()
    res=a+r*(b-a)
    
    return res

def uniformellegadas(a,b):
    r=random.random()
    res=a+r*(b-a) 
    return round(res,2)

def sumarlista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum

def acumulado(lista):
    dataacu=[]
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
        dataacu.append(sum)
    return dataacu

def uniformefallas(a,b):
    dato=[]
    sum=0
    a=True
    while(sum<=168):
        r=random.random()
        res=a+r*(b-a)
        sum=sum+res
        dato.append(round(res,2))
    return dato



def proa():
    f=[0.4,0.3,0.2,0.1]
    x=[1,2,5,10]
    sum=0
    n=0
    r=random.random()
    while sum<r:
        sum=sum+f[n]
        n+=1        
    return x[n-1]

fallas=uniformefallas(33,43)
fallas.pop()

print("fallas",fallas)
print("acumulado",acumulado(fallas))
listaacu=acumulado(fallas)
reparo=[]


for l in range(len(listaacu)):
    aux1=0
    aux=math.floor(listaacu[l]/12)
    if(aux%2==0):
        aux1=uniformereparo(3,7)
    else:
        aux1=uniformereparo(10,17)
    reparo.append(round(aux1,2))

print("tiempo de reparacion ",reparo)


print("llegadas")
datoslegada=[]

aux=0
i=0
hola=24*60*7
atencion=[]
while(aux<hola):
    r=uniformellegadas(4,6)
    aux=aux+r
    i+=1
    datoslegada.append(r)

print(datoslegada)
print("atencion")
aux=0
li=acumulado(fallas)
al=len(li)
##print(al)
f=0
reparar=0
auxi=1
for lol in range(al):
    auxl=0
    suma=0
    while(fallas[lol]*60>suma):
        pl= proa()
        suma+=datoslegada[auxi]+pl+reparar
        auxl=datoslegada[auxi]+pl+reparar
        atencion.append(round(auxl,3))
        auxi+=1
    reparar=reparo[lol]*60
        

atencion.pop()
print(atencion)
print("pedidos atendidos ",auxi)
print("pedidos en espera",len(datoslegada)-auxi)