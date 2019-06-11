from Calculadora import Calculadora

def menu():
    print("CALCULADORA\nPara continuar pulse c\nPara finalizar pulse f\n")


def menuOperaciones():
    print("Para sumar pulse +\nPara restar pulse -\nPara multiplicar pulse *\nPara dividir pulse /\n")

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
        calculadora = Calculadora(n1,n2)

        if operacion=='+': print(calculadora.n1," + ",calculadora.n2," = ",calculadora.sumar())
        elif operacion=='-': print(n1," - ",n2," = ",calculadora.restar())
        elif operacion=='*': print(n1," * ",n2," = ",calculadora.multiplicar())
        elif operacion=='/': print(n1," / ",calculadora.n2," = ",calculadora.dividir())
        