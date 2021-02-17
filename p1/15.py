import math
import random
import matplotlib.pyplot as plt

def geray(lista):
    dataacu=[]
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+1
        dataacu.append(sum)
    return dataacu


po=100000
ca=1
su=po-ca
p=0.7
cur=0
pcua=0.1
curados=[]
curados.append(cur)
pobla=[]
pobla.append(po)
Casos=[]
Casos.append(ca)
susep=[]
susep.append(su)
i=0
while(po>1):
    caux=round(pobla[i]*(1-p))
    print(caux)
    Casos.append(caux)
    po=pobla[i]-caux
    pobla.append(po)
    su=pobla[i]-caux
    susep.append(su)
    if(i>0):
        curados.append(round(Casos[i-1]*pcua))
    
    i+=1
print("poblacion",pobla)
print("casos",Casos)
print("suspuesto ",susep)

print("curados ",curados)



plt.title('resultados')
plt.plot(pobla,"y",Casos,"g",susep,"r",curados,"c")
plt.show()

plt.title('poblacion')
plt.plot(pobla,"y",)
plt.show()

plt.title('casos')
plt.plot(Casos,"g")
plt.show()

plt.title('suseptibles')
plt.plot(susep,"r")
plt.show()

plt.title('curados')
plt.plot(curados,"c")
plt.show()