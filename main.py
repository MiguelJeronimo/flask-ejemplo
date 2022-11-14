import pymysql
from app import app
from connection_db import mysql
from flask import flash,request,jsonify

#Creando rutas que reciben valores
@app.route('/api/<dato>')
def hello(dato):
    return 'Hola %s!'% dato
#app.add_url_rule('/','hello', hello)
#creando rutas sin parametros
@app.route('/api/saludo')
def saludo():
    return "hola todos"

#Muestra todos los productos de la tabla producto en mysql
@app.route('/api/productos')
def Productos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM producto;")
        rows = cursor.fetchall()
        return jsonify(rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
   #app.run()
   app.run(debug=True)