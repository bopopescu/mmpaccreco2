import mysql.connector


class Conexion:

    def __init__(self):
        self.miconexion=mysql.connector.connect(host="localhost", user="root", passwd="",database="mmarticulos")