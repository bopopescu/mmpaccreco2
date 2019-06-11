import pymysql
from flask import Flask 
from flask import jsonify
from flask import flash, request
from Conexion import Conexion

app = Flask(__name__)

@app.route('/articulos')
def articulos():
	try:
	#	conn = mysql.connect()
	#	cursor = conn.cursor(pymysql.cursors.DictCursor)
		oConexion = Conexion().miconexion
		cursor = oConexion.cursor()
		cursor.execute("select * from articulos")
		filas = cursor.fetchall()
		resp = jsonify(filas)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		oConexion.close()

@app.route('/articulosdiccionario')
def articulosdiccionario():
	try:
	#	conn = mysql.connect()
	#	cursor = conn.cursor(pymysql.cursors.DictCursor)
		oConexion = Conexion().miconexion
		cursor = oConexion.cursor(pymysql.cursors.DictCursor)
		cursor.execute("select codigo,descripcion,precio from articulos")
		filas = cursor.fetchall()
		resp = jsonify(filas)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		oConexion.close()


app.run(debug = False, port=10000)
