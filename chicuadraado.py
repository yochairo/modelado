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
        if(a[0]==l):
            sum+=1
    return sum
    


def hmedia(lista):
    sum=0.0
    suf=0.0
    for i in range(0,len(lista)):
        sum=sum+i*lista[i]
        suf=suf+lista[i]
     
    return sum/suf


xls=pd.ExcelFile('practica autos.xlsx')
print(xls.sheet_names)
df=xls.parse()

lf=[]
lf=df.values.tolist()

#print(lf)
fec=[]
for i in range(100):
    
    a=hayn(lf,i)
    fec.append(a)

#print(fec)
print(len(fec))

for i in range(100):
    print(i,fec[i])

media=hmedia(fec)
print(media)
chit=0
sumat=0
for k in range(100):
    
    chit+=math.pow((fec[i]-299*poison(media,k)),2)/(299*poison(media,k))
 

chidetablas=129.56



print("poison ")
print(chit)
if(chidetablas>chit):
    print("los datos no coresponde a la fdp")
else:
    print("los datos coresponde a la fdp")


chicuadrado=0
for k in range(100):
    chicuadrado+=math.pow((fec[i]-299*binomial(99,media,k)),2)/(299*binomial(99,media,k))
   


print("binomial")
print(chicuadrado)
if(chidetablas>chicuadrado):
    print("los datos no coresponde a la fdp")
else:
    print("los datos coresponde a la fdp")




chicuadradoe=0
for k in range(100):
    chicuadradoe+=math.pow((fec[i]-299*(1/99)),2)/(299*(1/99))
   


print("equiporbable")
print(chicuadradoe)
if(chidetablas>chicuadradoe):
    print("los datos no coresponde a la fdp")
else:
    print("los datos coresponde a la fdp")