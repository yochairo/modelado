import math
import random
import time 
def rand(s,m,n):
    sem=random.random()
    ret =0.0
    inte=0.0
    dx=6*s/n
    i=1
    while(inte<sem):
        ret=i*dx
        inte+=math.exp(-(pow(math.log(ret)-m,2)/(2*s*s)))*dx/(s*ret*math.sqrt(2*math.pi))
        i+=1
    return ret

dato=[]
s=float(input("sigma"))
m=float(input("media"))
n=float(input("n"))
for i in range(100):
   dato.append(rand(s,m,n))
print(dato)