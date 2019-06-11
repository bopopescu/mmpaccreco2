from flask import Flask
#este import es para que reciba parámetros
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola hola run.py'

#http://localhost:10000/saluda
@app.route('/saluda')
def saluda():
    return 'un saluda'

#ruta por defecto
@app.route('/parametros/')
#http://localhost:10000/parametros/
#Parámetro 1: nombre-default. Parámetro 2: numero-default
#############################################
#ruta con un parámetro de tipo string
@app.route('/parametros/<nombre>/')
#http://localhost:10000/parametros/libros/
#Parámetro 1: libros. Parámetro 2: numero-default
#############################################
#ruta con un primer parámetro de tipo string y un segundo parámetro de tipo int
#http://localhost:10000/parametros/libros/1
#Parámetro 1: libros. Parámetro 2: 1
@app.route('/parametros/<nombre>/<int:numero>')
def parametros(nombre='nombre-default', numero='numero-default'):
    return 'Parámetro 1: {}. Parámetro 2: {}'.format(nombre, numero)

if(__name__ == '__main__'):
    app.run(debug=True, port=10000)