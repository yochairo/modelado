import math
import random
p = float(input("p "))
q=1-p
datos=[]
sum1=0
a=0
for l in range(0,2):
    sum1=math.pow(p,l)*math.pow(1-p,1-l)
    print(sum1)
for j in range(1000):
    r=random.random()
    i=0
    sum=0
    while sum<r:
        sum=sum+math.pow(p,i)*math.pow(1-p,1-i)
        i=i+1
    datos.append(i)
print(datos)    
