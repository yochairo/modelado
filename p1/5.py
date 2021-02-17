import math 
import random
import matplotlib.pyplot as plt
import numpy as np

y=[]
x=[]
ti=[]
r2=[]
for i in range(20000):
    u1=random.random()
    R2=-math.log10(u1)
    tita=2*math.pi*random.random()
    xa=math.sqrt(2*R2)*math.cos(tita)
    ya=math.sqrt(2*R2)*math.sin(tita)
    y.append(ya)
    x.append(xa)
    ti.append(tita)
    r2.append(R2)


plt.title('x')
plt.hist(x)
plt.show()

plt.title('y')
plt.hist(y)
plt.show()
#
#plt.plot(r2,y,'ro')
#plt.plot(ti,x,'bs')
#plt.show()
#
