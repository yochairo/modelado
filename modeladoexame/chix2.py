import pandas as pd
import math

def poison (lam,l):
    sum1=math.exp(-lam)*math.pow(lam,l)/math.factorial(l)
    
    return sum1

def binomial(n,media,l):
    p=media/n
    q=1-p
    b=math.pow(p,l)*math.pow(q,n-l)
    sum1=math.factorial(n)/(math.factorial(l)*math.factorial(n-l))*b
    return sum1

def hayn(lista,l):
    sum=0.0
    for i in range(0,len(lista)):
        a=lista[i]
        if(a==l):
            sum+=1
    return sum
    


def hmedia(lista):
    sum=0.0
    suf=0.0
    for i in range(0,len(lista)):
        sum=sum+i*lista[i]
        suf=suf+lista[i]
     
    return sum/suf


lf=[14, 10, 12, 13, 11, 11, 9, 14, 10, 13, 11, 7, 16, 5, 19, 17, 10, 4, 8, 13, 12, 16, 14, 18, 11, 7, 9]

print(lf)
tama=len(lf)
fec=[]
for i in range(min(lf),max(lf)):
    
    a=hayn(lf,i)
    fec.append(a)

#print(fec)
print(len(fec))

for i in range(len(fec)):
    print(i,fec[i])

media=hmedia(fec)
print(media)
chit=0
sumat=0
for k in range(len(fec)):
    
    chit+=math.pow((fec[k]-tama*poison(media,k)),2)/(tama*poison(media,k))
 

chidetablas=30.43



print("poison ")
#print(chit)
if(chidetablas>chit):
    print("los datos no coresponde a la fdp")
else:
    print("los datos coresponde a la fdp")


chicuadrado=0
for k in range(len(fec)):
    chicuadrado+=math.pow((fec[k]-tama*binomial(max(lf),media,k)),2)/(tama*binomial(max(lf),media,k))
   


print("binomial")
#print(chicuadrado)
if(chidetablas>chicuadrado):
    print("los datos no coresponde a la fdp")
else:
    print("los datos coresponde a la fdp")




chicuadradoe=0
for k in range(len(fec)):
    chicuadradoe+=math.pow((fec[k]-tama*(1/max(lf))),2)/(tama*(1/max(lf)))
   


print("equiporbable")
#print(chicuadradoe)
if(chidetablas>chicuadradoe):
    print("los datos no coresponde a la fdp")
else:
    print("los datos coresponde a la fdp")