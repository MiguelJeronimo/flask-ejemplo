#usando la liberia flask-mysql
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

#configurando la conección a la base de datos
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mike123'
app.config['MYSQL_DATABASE_DB'] = 'tienda'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
