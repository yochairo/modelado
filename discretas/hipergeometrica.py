import math
import random

n = int(input("n "))
m = int(input("m "))
p = float(input("p "))
q=1-p
datos=[]
sum1=0
def combina(m, n):
    
    return math.factorial(m) / (math.factorial(n) * math.factorial(m - n))

for j in range(1000):
    r=random.random()
    i=0
    sum=0
    while sum<r:
        sum=sum+combina(m*p,i)*combina(m*(1-p),n-i)/combina(m,n)
        i=i+1
    datos.append(i)
print(datos)
for l in range(0,n):
    sum1=combina(m*p,l)*combina(m*(1-p),n-l)/combina(m,n)
    print(l," ",sum1)