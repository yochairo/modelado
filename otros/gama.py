import random
import math

alfa = int(input("alfa "))
beta = float(input("beta "))

rand=random.random()
i=0.0
sum=0
while sum <rand:
    sum=sum+math.pow(i*ax,alfa-1)*math.pow(1-i*ax,beta-1)
    i+=1
    

##print(math.gamma(-1))
