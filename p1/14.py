import math
import random
def funciof():
    r=random.random()
    aux=1-math.exp(-r)
    return aux



def funciong():
    r=random.random()
    aux=1-math.exp(-3*r)
    return aux

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)

t=[]
for ll in range(1000):
    n=5
    listan=[n]
    s=3
    listas=[s]
    d=0
    listad=[d]
    ini=n+s
    i=0
    while (n>1):
        aux=n-round(n*funciof())
    
        if(aux<=s):
            reparo=listad[i]*funciong()
            s=s-aux+reparo
            listan.append(n)
            listas.append(s)
            listad.append(aux+listad[i]-reparo)
        else:
            reparo=listad[i]*funciong()
            n=n-aux+round(reparo)
            listan.append(n)
            listad.append(aux+listad[i]-reparo)
        i+=1
    t.append(i)
    print(i)
print(t)
print("esperanza",promediarLista(t))



