def menu():
    print("CALCULADORA\nPara continuar pulse c\nPara finalizar pulse f")


def menuOperaciones():
    print("Para sumar pulse +\nPara restar pulse -\nPara multiplicar pulse *\nPara dividir pulse /\n")

def sumar(n1,n2):
    return n1+n2

def restar(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    while n2==0:
        n2=float(input('n2?'))
    return n1/n2

#main
continuar = True
opcion=""
while continuar:
    menu()
    opcion=input()
    while opcion!='c' and opcion!='f':
        menu()
        opcion=input()
    if opcion == 'f': continuar=False
    else:
        menuOperaciones()
        operacion=input()
        operaciones=('+','-','*','/')
        while operacion not in operaciones:
            menuOperaciones()
            operacion=input()
        n1=float(input("n1?"))
        n2=float(input("n2?"))
        if operacion=='+': print(n1," + ",n2," = ",sumar(n1,n2))
        elif operacion=='-': print(n1," - ",n2," = ",restar(n1,n2))
        elif operacion=='*': print(n1," * ",n2," = ",multiplicar(n1,n2))
        elif operacion=='/': print(n1," / ",n2," = ",dividir(n1,n2))
