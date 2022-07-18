import mysql.connector

def create_database():
    usuario = input("Ingrese su usuario de MariaDB: ")
    contraseña = input ("Ingrese su contraseña de MariaDB: ")
    while True:
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "usuario",
                password = "contraseña"
            )
            break
        except:
            print("Usuario o contraseña incorrectos, por favor, ingreselos nuevamente.")
            usuario = input("Ingrese su usuario de MariaDB: ")
            contraseña = input ("Ingrese la contraseña de MariaDB: ")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS 9Region")
    return usuario, contraseña

def create_tables(usuario, contraseña):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "usuario",
        password = "contraseña",
        database = "9Region"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS MedioDePrensa (id_medio INT AUTO_INCREMENT PRIMARY KEY, nombre_mp VARCHAR(25), fecha_mp DATE, url_mp VARCHAR(25), region INT, pais VARCHAR(25), idioma VARCHAR(25)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS dueños (id_dueños INT AUTO_INCREMENT PRIMARY KEY, nombre_d VARCHAR(25), empresa VARCHAR(25), fecha_d DATE, nombre_mp VARCHAR(25))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Noticia (id_noticia INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(25),cuerpo VARCHAR(255),fecha_n DATE,url_n VARCHAR(255)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Mencionado (id_persona INT AUTO_INCREMENT PRIMARY KEY, nombre_m VARCHAR(25), profesion VARCHAR(25), nacimiento DATE, nacionalidad VARCHAR(25), popularidad INT")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Mencionar (id_noticia INT, id_persona INT, PRIMARY KEY (id_noticia,id_persona))")

def create_foreign_keys(usuario, contraseña):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "usuario",
        password = "contraseña",
        database = "9Region"
    )
    mycursor = mydb.cursor()
    mycursor.execute("""
    alter table noticia  
    add constraint fk1
    foreign key(id_medio) 
    references MedioDePrensa(id_medio)
    on delete set null
    on update set null
    """)

def insert_data(usuario, contraseña):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "usuario",
        password = "contraseña",
        database = "9Region"
    )
    mycursor = mydb.cursor()
    tabla = input("Ingrese el nombre de la tabla a la que quiere agregar datos (MedioDePrensa, noticia, dueños, personas): ")
    if (tabla == "MedioDePrensa"):
        nombre = input ("Ingrese el nombre del medio de prensa: ")
        fecha = input ("Ingrese la fecha de creación del medio prensa YYYY-MM-DD: ")
        url = input ("Ingrese la url del medio de prensa: ")
        region = input ("Ingrese la region del medio de prensa (en numeros romanos): ")
        pais = input ("Ingrese el país del medio de prensa: ")
        idioma = input ("Ingrese el idioma del medio de prensa: ")
        tipo = input ("Ingrese el tipo del medio de prensa (regional o local): ")
        val = (nombre, fecha, url, region, pais, idioma, tipo)
        sql = ("INSERT INTO MedioDePrensa (nombre_mp, fecha_mp, url_mp, region, pais, idioma) VALUES (%s, %s, %s, %s, %s, %s)")
        mycursor.execute (sql,val)
        mydb.commit()

    if (tabla == "Dueño"):
        nombre = input("Ingrese el nombre del dueño: ")
        tipo = input ("Ingrese el tipo (persona o empresa): ")
        fecha = input ("Ingrese la fecha de adquisición YYYY-MM-DD: ")
        val = (nombre, tipo, fecha)
        sql = "INSERT INTO Dueño (nombre_d, empresa, fecha_d,nombre) VALUES (%s, %s, %s)"
        mycursor.execute(sql,val)
        mydb.commit()

    if (tabla == "Noticia"):
        url = input("Ingrese la url de la noticia: ")
        titulo = input("Ingrese el titulo de la noticia: ")
        fecha = input("Ingrese la fecha de publicacion de la noticia YYYY-MM-DD: ")
        contenido = input ("Ingrese el contenido de la noticia: ")
        val = (url, titulo, fecha, contenido)
        sql = ("INSERT INTO Noticia (titulo, cuerpo, fecha_n, url_n) VALUES (%s, %s, %s, %s)")
        mycursor.execute(sql, val)
        mydb.commit()

    if (tabla == "Mencionado"):
        nombre = input ("Ingrese el nombre de la persona: ")
        profesion = input ("Ingrese la profesion de la persona: ")
        fecha = input ("Ingrese la fecha de nacimiento de la persona YYYY-MM-DD: ")
        nacionalidad = input ("Ingrese la nacionalidad de la persona: ")
        popularidad = input ("Ingrese la popularidad de la persona: ")
        val (nombre, profesion, fecha, nacionalidad, popularidad)
        sql = "INSERT INTO Mencionado (nombre_m, profesion, nacimiento, nacionalidad, popularidad) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql,val)
        mydb.commit()

    

def main():
    usuario, contraseña = create_database()
    create_tables(usuario, contraseña)
    try:
        create_foreign_keys(usuario, contraseña)
    except:
        print ("Las claves foráneas ya han sido creadas")
    print("La base de datos se ha creado correctamente")
    pregunta = input("Le gustaría ingresar datos? S/N= ")
    if (pregunta == "S"): pregunta = True
    else: 
        pregunta = False
        print("El programa ha finalizado")
    while (pregunta):
        insert_data(usuario, contraseña)
        pregunta = input("Le gustaría ingresar datos? S/N= ")
        if (pregunta == "S"): pregunta = True
        if (pregunta == "N"): 
            pregunta = False
            print("El programa ha finalizado")
main()  