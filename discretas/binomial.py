import math
import random

n = 15
me=2
p = me/n
q=1-p
datos=[]
sum1=0
a=0
for l in range(0,n):
    b=math.pow(p,l)*math.pow(q,n-l)
    sum1=math.factorial(n)/(math.factorial(l)*math.factorial(n-l))*b
    print(l," ",sum1)
for j in range(90):
    r=random.random()
    i=0
    sum=0
    while sum<r:
        b=math.pow(p,i)*math.pow(q,n-i)
        sum=sum+math.factorial(n)/(math.factorial(i)*math.factorial(n-i))*b
        i=i+1
    datos.append(i)
print(datos)    
