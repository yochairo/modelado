import math
import random
import matplotlib.pyplot as df
import pandas as pd



lam = float(input("landa"))

datos=[]
sum1=0
a=0
for l in range(0,20):
    sum1=math.exp(-lam)*math.pow(lam,l)/math.factorial(l)
    print(l," ",sum1)

for j in range(27):
    r=random.random()
    i=0
    sum=0
    while sum<r:
        sum=sum+math.exp(-lam)*math.pow(lam,i)/math.factorial(i)
        i=i+1
    datos.append(i)
print(datos)  
