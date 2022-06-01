import pymysql

Host = "localhost"
User =
Password = ""

conn = pymysql.connect(host=Host, user=User, password=Password)
cur = conn.cursor()

cur.execute("CREATE DATABASE 9Region")
cur.execute("""CREATE TABLE MedioDePrensa(
            nombre_mp VARCHAR(25),
            fecha_mp DATE,
            url_mp VARCHAR(25),
            region INT,
            pais VARCHAR(25),
            idioma VARCHAR(25)
            )""")
cur.execute("""CREATE TABLE Dueño(
            nombre_d VARCHAR(25),
            empresa BOOLEAN,
            fecha_d DATE,
            nombre_mp VARCHAR(25)
            )""")
cur.execute("""CREATE TABLE Noticia(
            titulo VARCHAR(25),
            cuerpo VARCHAR(255),
            fecha_n DATE,
            url_n VARCHAR(255)
            )""")
cur.execute("""CREATE TABLE Mencionado(
            nombre_m VARCHAR(25),
            profesion VARCHAR(25),
            nacimiento DATE,
            nacionalidad VARCHAR(25),
            popularidad INT
            )""")
cur.execute("""CREATE TABLE Mencionar(
            titulo VARCHAR(25),
            nombre_m VARCHAR(25)
            )""")
conn.commit()         
conn.close()