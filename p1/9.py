import math
import random
def expo(lan):
    media=1/lan
    r=random.random()
    res=-media*math.log(1-r)   
    return math.ceil(res)

def a():
  
    f=[1/6,1/6,1/6,1/6,1/6,1/6]
    x=[1,2,3,4,5,6]
    sum=0
    n=0
    r=random.random()
    while sum<r:
        sum=sum+f[n]
        n+=1           
    return x[n-1]

def haynum(lista,n):
    sum=0.0
    for i in range(0,len(lista)):
        if(lista[i]==n):
            sum+=1
    return sum 

def b():
  
    f=[1/2,1/2]
    x=[1,2]
    sum=0
    n=0
    r=random.random()
    while sum<r:
        sum=sum+f[n]
        n+=1           
    return x[n-1] 
def suma(lista):
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

def bernuli(p,l):
    datos=[]
    for j in range(l):
        r=random.random()
        i=0
        sum=0
        while sum<r:
            sum=sum+math.pow(p,i)*math.pow(1-p,1-i)
            i=i+1
        datos.append(i)
    return datos

def uniforme(a,b):
    r=random.random()
    res=a+r*(b-a) 
    return round(res)

llegadas=[]
i=0

while(i<60*10):
    r=uniforme(1,3)
    llegadas.append(r)
    i+=r
###
#print(llegadas)
#print(suma(llegadas))
#print(acumulado(llegadas))
#print(len(llegadas))
###

articulos=[]
for l in range(len(llegadas)):
    al=expo(1/12)
    articulos.append(al)
print ("articulos ",articulos)
f=acumulado(llegadas)
antecioncajas =bernuli(0.04,len(llegadas))
terseaedad=[]
print(len(llegadas),len(articulos))
for ll in range(len(llegadas)):
    
    if(antecioncajas[ll]==2):
        aux=[f[ll],articulos[ll],f[ll]+6]
        #aux.append(f[ll])
        #aux.append(articulos[ll])
        #aux.append(f[ll]+6)
        terseaedad.append(aux)
        articulos.pop(ll)
        f.pop(ll)
        llegadas.pop(ll)

print(articulos,llegadas)
print(len(llegadas),len(articulos))

print("llegada","cantida  articulos "," total tardado","                  caja        ","salida")

cajas=[]
cajasr=[]
for k in range(len(llegadas)):
    if(articulos[k]>5):
        r=a()
        cajas.append(r)
        print(f[k],"      ",articulos[k],"                 ",round(articulos[k]+articulos[k]*6/60,2),"                 caja normal",r,"       ",f[k]+articulos[k]+articulos[k]*6/60)
    else:
        r=b()
        cajasr.append(r)
        print(f[k],"      ",articulos[k],"                 ",round(articulos[k]+articulos[k]*5/60,2),"                 caja rapida",r,"       ",f[k]+articulos[k]+articulos[k]*5/60)
print("clientes caja espesial", len(terseaedad))
print(terseaedad)

print("clientes en 1 ",haynum(cajas,1))

print("clientes en 2 ",haynum(cajas,2))

print("clientes en 3 ",haynum(cajas,3))

print("clientes en 4 ",haynum(cajas,4))

print("clientes en 5 ",haynum(cajas,5))

print("clientes en 6 ",haynum(cajas,6))



print("clientes en caja rapida 1 ",haynum(cajasr,1))

print("clientes en caja rapida 2",haynum(cajasr,2))


