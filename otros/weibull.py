import random
import math

alfa = float(input("alfa "))
beta = float(input("beta "))
datos= []
for i in range(100):
    rand=random.random()
    x=pow(-math.log(rand)*pow(beta,alfa),1/alfa)
    datos.append(x)
    print(x)
