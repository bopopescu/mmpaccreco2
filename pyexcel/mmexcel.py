import pandas as pd
import numpy as np
#df = pd.DataFrame()
#print(df)
#IR A LÍNEA 189
'''
A PARTIR DE UN ARCHIVO EXCEL OBTENGO SU CONTENIDO Y LO GUARDO EN UNA LISTA.
DICHA LISTA ESTÁ FORMADA POR LISTAS QUE SE CORRESPONDE CON CADA FILA DEL ARCHIVO EXCEL
DESPUÉS CREO OTRA LISTA QUE VA A TENER CADA FILA EN EN EL QUE TENGA UN ELEMENTO PAR
lista = pd.read_excel('mmexcel.xlsx').values.tolist() 
print(lista)
[[1, 2, 3], [11, 33, 55], [11, 20, 33], [5, 9, 10], [11, 15, 17], [77, 99, 11], [55, 77, 99], [99, 99, 99], [5, 7, 9], [9, 7, 2]]

filasNumerosPares = []

for fila in lista:
  for i in fila:
    if(i%2==0):
      filasNumerosPares.append(fila)

print(filasNumerosPares) 
#[[1, 2, 3], [11, 20, 33], [5, 9, 10], [9, 7, 2]]

'''
mmlista = pd.read_excel('mmexcel2.xlsx').values.tolist()
print("muestro mmlista")
print(mmlista)
auxmmlista = []
for fila in mmlista:
  for f in fila:
    if(f%2==0): 
      auxmmlista.append(fila)
      break
print("muestro auxmmlista")
print(auxmmlista)
'''
Empty DataFrame
Columns: []
Index: []
'''
#archivoExcel = pd.read_excel('c:/excelpython/ejemplo2.xlsx')
#print(archivoExcel)
'''
        LOL Unnamed: 1 Unnamed: 2
0       NaN        NaN        NaN
1  posicion     tier 1      tier2
2       top     darius        jax
3      jung         j4    lee sin
4       mid     viktor        zed
5       adc      varus      vayne
6      supp    alistar      leona
'''
#archivoExcel = pd.read_excel("ejemplo2.xlsx")   #muestra la pestaña 1
#archivoExcel = pd.read_excel("ejemplo2.xlsx","Sheet2")
#print(archivoExcel)
'''
    esto   es    una    prueba
0    NaN   NaN   NaN       NaN
1  para    ver  c�mo  funciona
2    NaN   NaN   NaN       NaN
3    pd.  read     _     excel
4    sin  usar  xlrd       NaN
'''
#print(type(archivoExcel))   #<class 'pandas.core.frame.DataFrame'>

#print(archivoExcel.esto)
'''
0      NaN
1    para 
2      NaN
3      pd.
4      sin
'''
#print(archivoExcel.prueba)
'''
prueba
0 
 NaN
1  funciona
'''
#print(list(archivoExcel.Columns))   #AttributeError: 'DataFrame' object has no attribute 'Columns'

#print(archivoExcel[0])

##########################
#df = pd.read_excel("ejemplo2.xlsx")
#print(df)
'''
  posicion   tier 1    tier2
0      top   darius      jax
1     jung       j4  lee sin
2      mid   viktor      zed
3      adc    varus    vayne
4     supp  alistar    leona
'''
#df = pd.read_excel("ejemplo2.xlsx", header=None)
#print(df)
'''
          0        1        2
0  posicion   tier 1    tier2
1       top   darius      jax
2      jung       j4  lee sin
3       mid   viktor      zed
4       adc    varus    vayne
5      supp  alistar    leona
'''

#df = pd.read_excel("ejemplo2.xlsx", header=None)
#print(df[0])    #ídem para 1 y para 2
'''
0    posicion
1         top
2        jung
3         mid
4         adc
5        supp
Name: 0, dtype: object
'''
#df = pd.read_excel('ejemplo2.xlsx')
#print(df.Columns)   #AttributeError: 'DataFrame' object has no attribute 'Columns'

#df = pd.read_excel('ejemplo2.xlsx', columns=['col0','col1','col2'])
#df.to_excel('hejemplo2.xlsx',sheet_name='Hoja0')
#print(pd.read_excel('hejemplo2.xlsx',sheet_name='Hoja0'))
'''
   Unnamed: 0 posicion   tier 1    tier2
0           0      top   darius      jax
1           1     jung       j4  lee sin
2           2      mid   viktor      zed
3           3      adc    varus    vayne
4           4     supp  alistar    leona
'''
#df = pd.read_excel('hejemplo2.xlsx')
#print(df.columns)   #Index(['Unnamed: 0', 'posicion', 'tier 1', 'tier2'], dtype='object')

#df = pd.read_excel('ejemplo2.xlsx')   #Index(['posicion', 'tier 1', 'tier2'], dtype='object')
#print(df.columns)
#print(df['posicion'])
'''
Index(['posicion', 'tier 1', 'tier2'], dtype='object')
0     top
1    jung
2     mid
3     adc
4    supp
Name: posicion, dtype: object
'''
#df = pd.read_excel('ejemplo2.xlsx')
#print(df.iloc[[0]])
'''
  posicion  tier 1 tier2
0      top  darius   jax
'''
#df = pd.read_excel('ejemplo2.xlsx',header=None)
#print(df.iloc[[0]])
'''
          0       1      2
0  posicion  tier 1  tier2
'''
#df = pd.read_excel('ejemplo2.xlsx')
#aux = df.loc[[0]]
#print(df.loc[[0]])
'''
  posicion  tier 1 tier2
0      top  darius   jax
'''
#df = pd.read_excel('ejemplo2.xlsx',header=None)
#print(df.loc[[0]])
'''
          0       1      2
0  posicion  tier 1  tier2
'''
#df = pd.read_excel('ejemplo2.xlsx')
#print(df.loc[df[0]=='jax'])
#print(df.loc[0]=='jax')
'''
posicion    False
tier 1      False
tier2        True
Name: 0, dtype: bool
'''
#print(df.loc[0]=='darius')
'''
posicion    False
tier 1       True
tier2       False
Name: 0, dtype: bool
'''
#print(len(df.index))  #
#print(df.iloc[2:4])
'''
  posicion  tier 1  tier2
2      mid  viktor    zed
3      adc   varus  vayne
'''
#df = pd.read_excel('mmexcel.xlsx')
# Iteración por filas del DataFrame:
#for i,fila in df.iterrows():
  #print(i)
  #print(fila) #muestra cada fila
#print(df)

#print(len(df.columns))  #3

#aux = df.loc[1]
#print(aux.iat[0]) #1
#print(aux.iat[1])
'''
for i in aux:
  print(aux.iat[i-1])
'''
'''
for fila in aux.iterrows():
  print(type(i))
'''

#df = pd.read_excel('mmexcel.xlsx')
#lista = df.values.tolist()

#convierto el contenido de un excel en una lista
#lista = pd.read_excel('mmexcel.xlsx').values.tolist() 
#print(type(lista))  #<class 'list'>
#print(lista)
#[[1, 2, 3], [11, 33, 55], [11, 20, 33], [5, 9, 10], [11, 15, 17], [77, 99, 11], [55, 77, 99], [99, 99, 99], [5, 7, 9], [9, 7, 2]]



'''
for fila in lista:
  filasNumerosPares.append(list(filter(lambda i: i%2==0, fila)))

print(filasNumerosPares)   #[[2], [], [20], [10], [], [], [], [], [], [2]]
'''
filasNumerosPares = []
#results = [x*2 for x in A if x*2%3==0]
'''
personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]
personas_mayores=[per for per in personas if per[1]>=18]
'''
'''
for fila in lista:
  print(list(f for f in fila if f%2==0))  #hace lo mismo que list filter lambda de arriba
  #print(f for f in fila if f%2==0)
  #filasNumerosPares.append(fila(lambda i: i%2==0))
'''
#results.append((lambda x:x*2)(x))
'''
for fila in lista:
  filasNumerosPares.append(list(map(lambda i: i%2==0, fila))==True)

print(filasNumerosPares)  #[False, False, False, False, False, False, False, False, False, False]
'''
#results = filter(lambda x:x*2%3==0, map(lambda x:x*2, A))
'''
for fila in lista:
#  filasNumerosPares.append(list((map(lambda n:n%2==0, fila), fila))) #lo devuelve todo
  filasNumerosPares= list(filter))
'''
'''
cuadrados = [x**2 for x in range(10) if x%2==0]
print(cuadrados)  #[0, 4, 16, 36, 64]
'''
#filasNumerosPares=[pares for pares in lista if(filter(lambda n:n%2==0, pares))]
#print(filasNumerosPares)
'''
for fila in lista:
  filasNumerosPares.append(list(pares for pares in fila if(pares%2==0)))

print(filasNumerosPares)  #[[2], [], [20], [10], [], [], [], [], [], [2]]
'''
lista = pd.read_excel('mmexcel2.xlsx').values.tolist() 
for fila in lista:
  #filasNumerosPares.append(list(pares for pares in fila if(lambda n:pares[n]%2==0)))
  for f in fila:
    if(f%2==0):
      filasNumerosPares.append(fila)

print(filasNumerosPares)  #[[1, 2, 3], [2, 20, 33], [2, 20, 33], [5, 9, 10]]
print(type(filasNumerosPares))  #<class 'list'>
filasNumerosPares=pd.DataFrame(filasNumerosPares).drop_duplicates()
print("muestro el dataframe")
print(type(filasNumerosPares))  #<class 'pandas.core.frame.DataFrame'>
print(filasNumerosPares)
'''
print()
print("muestro el dataframe sin filas duplicadas")
filasNumerosPares = filasNumerosPares.drop_duplicates()
print(filasNumerosPares)
'''
'''
print()
print()
print()

mmlista = pd.read_excel('mmexcel2.xlsx').values.tolist()
print("muestro mmlista")
print(mmlista)
auxmmlista = []
for fila in mmlista:
  for f in fila:
    if(f%2==0): 
      auxmmlista.append(fila)
      break
print("muestro auxmmlista")
print(auxmmlista)
'''