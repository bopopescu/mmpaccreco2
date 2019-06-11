def sumaTipada(n1:float,n2:float)->float:
    return n1+n2


def suma2(n1:int,n2:int)->float:
    return n1/n2


def suma3(n1:float,n2:float)->int:
    return n1/n2

#main
#print(suma2("5","6"))   #así peta. Motivo: TypeError: unsupported operand type(s) for /: 'str' and 'str'
print(suma2(5.0,6.0))   #así no peta. 0.83333333
print(suma2(5.5,6.5))   #así no peta. 0.846153846153....
print(suma2(5,10))      #0.5

#print(suma3("4","2"))   #así no deja porque no permite str
print(suma3(2,3))       #0.6666666666666666

'''
n1=input("n1?")
n2=input("n2?")
suma=n1+n2
print(f"{n1} + {n2} = {n1+n2}")
print(suma)
auxN1=float(n1)
print(type(auxN1))
auxN2=float(n2)
print(type(auxN2))
print(sumaTipada(auxN1,auxN2))
print(sumaTipada(float(n1),float(n2)))

n10:int = "5"
print(type(n10))    #<class 'str'> #por lo que veo no le importa :int
'''
