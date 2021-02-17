import pandas as pd
import math

def media(lista):
    sum=0.0
    suf=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
     
    return sum/len(lista)

def varianza(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+math.pow((lista[i]-media(lista)),2)
    return sum/(len(lista))

xls=pd.ExcelFile('DATOS2.xlsx')
print(xls.sheet_names)
df=xls.parse()

lf=[]
lf=df.values.tolist()

#print(lf)

reales=[]
simulados=[]
for i in range(len(lf)):
    for j in range(len(lf[i])):
        if(j==0):
            reales.append(lf[i][j])
        
        if(j==2):
            simulados.append(lf[i][j])

print("reales varianza:",varianza(reales)," media:",media(reales))
print("optimizados varianza:",varianza(simulados)," media:",media(simulados))