from flask import Flask 
#para usar los templates hace falta el siguiente import
from flask import render_template
app = Flask(__name__)
#si la carpeta contenedora de templates se llama de otra manera,
#por ejemplo, prueba_template, entonces hay que poner:
# app = flask(__name__, template_folder = "prueba_template")
@app.route('/user/<name>')
def user(name='Amparo'):
    age = 18
    lstNumbers = [1,2,3,4,5,6]
#    return render_template('user.html')
    return render_template('user.html', nombre=name, edad=age, lstNumeros=lstNumbers)

if __name__ == '__main__':
    app.run(debug=True, port=10000)