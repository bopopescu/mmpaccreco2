import mysql.connector

class Conexion:

    def __init__(self):
        self.miconexion=mysql.connector.connect(host="localhost", user="root", passwd="",database="mmpy")

'''
def __init__(self):
        self.n1=0.0
        self.n2=0.0

cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()
'''