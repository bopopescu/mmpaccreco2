from flask import Flask 
#para usar los templates hace falta el siguiente import
from flask import render_template
app = Flask(__name__)
#si la carpeta contenedora de templates se llama de otra manera,
#por ejemplo, prueba_template, entonces hay que poner:
# app = flask(__name__, template_folder = "prueba_template")
@app.route('/')
def index():
    #return 'hola hola run.py'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=10000)