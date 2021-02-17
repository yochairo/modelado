import math 
import random

def a():
    dato=[]
    f=[0.10,0.30,0.45,0.15]
    x=[1,2,3,4]
    
    for i in range(1000):
        sum=0
        n=0
        r=random.random()
        while sum<r:
            sum=sum+f[n]
            n+=1
        
        dato.append(x[n-1])     
    return dato
print(a())