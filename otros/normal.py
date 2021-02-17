import random
import math
sig =float(input("sigma "))
media=float(input("media "))
ax=(6*sig)/100
datos= []
for j in range(20):
    rand=random.random()
    i=1
    sum=0
    while sum <rand:
        sum=sum +ax*(pow(2*math.pi*sig*sig,-0.5)*math.exp(-1*pow((i*ax-media)/sig,2)))
        i+=1
    
    
   ## datos.append(ax*i)    
    print(ax*i," fffff")