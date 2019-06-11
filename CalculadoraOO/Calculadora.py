class Calculadora:

    def __init__(self):
        self.n1=0.0
        self.n2=0.0

    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def sumar(self):
        return self.n1+self.n2

    def restar(self):
        return self.n1-self.n2

    def multiplicar(self):
        return self.n1*self.n2

    def dividir(self):
        while(self.n2==0):
            self.n2=float(input("n2?"))
        return self.n1/self.n2
    
    