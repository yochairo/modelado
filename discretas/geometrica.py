import math
import random
p = float(input("p "))
q=1-p
datos=[]
sum1=0
a=0
for l in range(1,10):
    sum1=p*math.pow(q,l-1)
    print(l," ",sum1)
for j in range(90):
    r=random.random()
    i=0
    sum=0
    while sum<r:
        sum=sum+p*math.pow(q,i-1)
        i=i+1
    datos.append(i)
print(datos)