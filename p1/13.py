import math 
import random
import matplotlib.pyplot as plt
def minimo(lista):
    min=lista[0]
    l=0
    for i in range(1,len(lista)):
        if(min>lista[i]):
            min=lista[i]
            l=i
    return l

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)
def varianza(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+math.pow((lista[i]-promediarLista(lista)),2)
    return sum/(len(lista)-1)
def desviaziontipica(lista):
    return math.sqrt(varianza(lista)) 

def uniforme(a,b):
    dato=[]
    for i in range(5000):
        r=random.random()
        res=a+r*(b-a)
        dato.append(res)
  
    return dato

def expo(lan):
    dato=[]
    for i in range(5000):
        r=random.random()
        res=-lan*math.log(1-r)
        dato.append(res)
   
    return dato

def a():
    dato=[]
    f=[10/85,17/85,14/85,35/85,9/85]
    x=[100,200,300,400,500]
    
    for i in range(5000):
        sum=0
        n=0
        r=random.random()
        while sum<r:
            sum=sum+f[n]
            n+=1
        
        dato.append(x[n-1])     
    return dato
def normalf():
    dato=[]
    for i in range(5000):
        r=random.random()
        x=(math.pow(r,0.135)-math.pow(1-r,0.135))/0.1975
        dato.append(x)  
    return dato

def swicia(i):
    switcher={
                0:'a,b^2,a,b,d^3,a',
                1:'a,b^2,a,a',
                2:'a,b^2+c+d^3,a'
           
             }
    return switcher.get(i,"Invalid ")
def swicib(i):
    switcher={
                0:'a,b^2,d^2,c',
                1:'a,c,e,a,c',
                2:'a,a,b^3,a,c'
               
             }
    return switcher.get(i,"Invalid ")

def swicic(i):
    switcher={
                0:'b,b^2,c,a^3,d,b^2',
                1:'b,b^2,a^3,d,b^2',
                2:'b,b^2,c,d,b^2'
             }
    return switcher.get(i,"Invalid ")

##plt.title('x')
#plt.hist(normalf())
#plt.show()
ma=promediarLista(a())
mb=promediarLista(expo(100))
mc=promediarLista(uniforme(52,435))
md=promediarLista(normalf())
me=promediarLista(expo(150))

print("a)")

s0=ma+mb*mb+ma+mb+(md**3)+ma
s1=ma+(mb**2)+ma+ma
s2=ma+mb**2+mc+md**3+ma

media=[s0,s1,s2]
print(media)
print("la ruta es ",swicia(minimo(media)),"con un total de ",media[minimo(media)])

print("b)")

b0=ma+(mb**2)+(md**2)+mc
b1=ma+mc+me+ma+mc
b2=ma+ma+(mb**3)+ma+mc

mediab=[b0,b1,b2]
print(mediab)
print("la ruta es ",swicib(minimo(mediab)),"con un total de ",mediab[minimo(mediab)])

print("c)")
c0=mb+(mb**2)+mc+(ma**3)+md+(mb**2)
c1=mb+(mb**2)+(ma**3)+md+(mb**2)
c2=mb+(mb**2)+mc+md+(mb**2)

mediac=[c0,c1,c2]
print(mediac)
print("la ruta es ",swicic(minimo(mediac)),"con un total de ",mediac[minimo(mediac)])
