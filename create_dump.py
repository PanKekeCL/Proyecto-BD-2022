import pymysql

Host = "localhost"
User = "usuario"
Password = "contraseña"
DB = input("Ingrese nombre de Database para clonar (\"9Region\"): ")

conn = pymysql.connect(host=Host, user=User, password=Password, database=DB)
cur = conn.cursor()

tables = []
for record in cur.fetchall():
	tables.append(record[0])

DumpName = DB + "_dump"
try:
	cur.execute(f'CREATE DATABASE {DumpName}')
except:
	pass

for t in tables:
	cur.execute(
		f'CREATE TABLE {t} SELECT * FROM {DB}.{t}')
        
print("Se ha creado la base de datos: ", DumpName)
conn.commit()         
conn.close()