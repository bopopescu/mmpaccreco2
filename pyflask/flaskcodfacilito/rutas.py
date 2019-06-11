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

#http://localhost:10000/parametros
#El parámetro es: valor por defecto: no existen datos para la consulta
#ahora he puesto la siguente url:
#http://localhost:10000/parametros?parametro1=buenas noches a todos
#http://localhost:10000/parametros?parametro1=buenas%20noches%20a%20todos
#El parámetro es: buenas noches a todos
#ahora he añadido un segundo parámetro:
#http://localhost:10000/parametros?parametro1=buenas noches&parametro2=a todos
#Parámetro 1: buenas noches. Parámetro 2: a todos
@app.route('/parametros')
def parametros():
    parametro1 = request.args.get('parametro1', 'valor por defecto: no existen datos para la consulta')
    parametro2 = request.args.get('parametro2', 'valor por defecto parámetro2')
    return 'Parámetro 1: {}. Parámetro 2: {}'.format(parametro1, parametro2)

if(__name__ == '__main__'):
    app.run(debug=True, port=10000)