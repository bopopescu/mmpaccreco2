from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo.'
    
#al parecer en environments no funciona el modo debug
app.run(debug = True, port=10000)