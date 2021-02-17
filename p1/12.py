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

def swici(i):
    switcher={
                0:'a,b,c,c,a',
                1:'a,b,d,b,c,a',
                2:'a,b,d,b,b,a',
                3:'a,b,d,c,c,a',
                4:'a,c,d,b,c,a',
                5:'a,c,d,b,b,a',
                6:'a,c,a,b,c,a',
                7:'a,c,a,b,b,a',
                8:'a,c,a,c,a'
             }
    return switcher.get(i,"Invalid day of week")

##plt.title('x')
#plt.hist(normalf())
#plt.show()
print("a")
print("media ",promediarLista(a()))
ma=promediarLista(a())
print("variaza ",varianza(a()))
print("desciacion tipica ",desviaziontipica(a()))

print("b")
print("media ",promediarLista(expo(100)))
mb=promediarLista(expo(100))
print("variaza ",varianza(expo(100)))
print("desciacion tipica ",desviaziontipica(expo(100)))

print("c")
print("media ",promediarLista(uniforme(52,435)))
mc=promediarLista(uniforme(52,435))
print("variaza ",varianza(uniforme(52,435)))
print("desciacion tipica ",desviaziontipica(uniforme(52,435)))

print("d")
print("media ",promediarLista(normalf()))
md=promediarLista(normalf())
print("variaza ",varianza(normalf()))
print("desciacion tipica ",desviaziontipica(normalf()))

print("e")
print("media ",promediarLista(expo(150)))
me=promediarLista(expo(150))
print("variaza ",varianza(expo(150)))
print("desciacion tipica ",desviaziontipica(expo(150)))

s1=ma+mb+mc+mc+ma
s2=ma+mb+md+mb+mc+ma
s3=ma+mb+md+mb+mb+ma
s4=ma+mb+md+mc+mc+ma
s5=ma+mc+md+mb+mc+ma
s6=ma+mc+md+mb+mb+ma
s7=ma+mc+ma+mb+mc+ma
s8=ma+mc+ma+mb+mb+ma
s9=ma+mc+ma+mc+ma

media=[s1,s2,s3,s4,s5,s6,s7,s8,s9]
print(media)
print("la ruta es ",swici(minimo(media)),"con un total de ",media[minimo(media)])