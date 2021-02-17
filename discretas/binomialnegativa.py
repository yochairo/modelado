import math
import random

k = int(input("k"))
p = float(input("p "))
q=1-p
datos=[]
sum1=0
def combina(m, n):
    return math.factorial(m) / (math.factorial(n) * math.factorial(m - n))

for l in range(0,50):
    sum1=combina(k+l-1,l)*math.pow(p,k)*math.pow(q,l)
    print(l," ",sum1)

for j in range(1000):
    r=random.random()
    i=0
    sum=0
    while sum<r:
        sum=sum+combina(k+i-1,i)*math.pow(p,k)*math.pow(q,i)
        i=i+1
    datos.append(i)
print(datos)
