import pymysql

Host = "localhost"
User = "usuario"
Password = "contraseña"

conn = pymysql.connect(host=Host, user=User, password=Password)
cur = conn.cursor()

cur.execute("USE 9Region;")
# 1) Cuantas noticias por cada medio de prensa.
print("Mostrando cantidad de Noticias por Medio de Prensa.")
cur.execute("SELECT count(*) Noticia GROUP BY nombre_mp;")

# 2) Quienes son las personas mencionadas en las noticias de un dia especifico.
dia = input("Ingrese una fecha en formato dd-mm-yyyy: ")
print("Mostrando personas mencionadas en Noticias del dia {dia}.")
cur.execute("SELECT DISTINCT nombre_m FROM Mencionado m JOIN Mencionar me ON m.nombre_m = me.nombre_m JOIN Noticia n ON me.titulo = n.titulo WHERE fecha_n = {dia};")

# 3) Como evoluciona la popularidad de una persona especifica
persona = input("Ingrese nombre de la persona: ")
print("Mostrando evolucion de popularidad de la persona {persona}.")
        # <-- AQUI FALTA COMPLETAR

# 4) Cuales son los 5 medios de prensa mas antiguos en una region especifica.
print("Mostrando los 5 medios de prensa mas antiguos de la 9ena Region.")
cur.execute("SELECT nombre_mp FROM MedioDePrensa ORDER BY fecha_mp DESC LIMIT 5;")