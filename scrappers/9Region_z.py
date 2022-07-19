import random
from requests_html import HTMLSession
# from pymongo import MongoClient
import time
import mysql.connector as mariadb
import sys
import datetime

#Formatear las fechas
def format_date(date):
    fecha = date.split("T")[0]
    fecha_split = fecha.split("-")
    # print(fecha_split)
    """ f = ""
    for i in range(len(fecha_split)-1,-1,-1):
        if(i == 0):
            f += fecha_split[i] 
        else:
            f += fecha_split[i] + "-"
         """
    return(fecha_split)

def formatoTexto(cuerpo):
    text = ""
    for i in range(0,len(cuerpo)):
        text += cuerpo[i] + "\n"
    return text

# Toma los datos en HTML de la URL y los añade a la DB.
def obtenerDatosUrl(url):
    session = HTMLSession()
    response = session.get("{}".format(url), headers = headers)

    xpath_fecha = "//div[@class='tdb-block-inner td-fix-index']/time/@datetime"
    fecha = response.html.xpath(xpath_fecha)
    fecha = format_date(fecha[0])

    xpath_titulo = "//div[@class='tdb-block-inner td-fix-index']/h1/text()"
    titulo = response.html.xpath(xpath_titulo)

    xpath_cuerpo = "//div[@class='tdb-block-inner td-fix-index']/p/text()" 
    cuerpo = response.html.xpath(xpath_cuerpo)
    texto = formatoTexto(cuerpo)

    print(fecha)
    fecha = datetime.date(int(fecha[0]), int(fecha[1]), int(fecha[2]))
    print(fecha)
    
    # print(datetime.date(int(fecha[2]),int(fecha[1]),int(fecha[0])))

    # INSERTANDO DATOS EN DB = 9Region.
    cur.execute("INSERT INTO noticia(url,titulo,cuerpo,fecha_publicacion) VALUES('{0}','{1}','{2}',{3})".format(url,titulo[0],texto,fecha)) #insertar datos en BD

# Conectarse a MariaDB.
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
cur = conn.cursor()

# Usaremos la base de datos 9Region.
cur.execute("USE 9Region")

session = HTMLSession()

# URL "SEED" que escrapear.
URL_SEED = "https://www.australtemuco.cl/"

# Simulamos que estamos utilizando un navegador web Mozilla.
USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


URL_PAGS = "https://www.australtemuco.cl/impresa/2022/07/17/full/cuerpo-principal/"
headers = {'user-agent':random.choice(USER_AGENT_LIST) }

## Analizar ("to parse") el cuerpo
xpath_url = "//div/h2[@class='entry-title']/a/@href"
# L_url = []
for i in range(1,12):
    if(i > 1):
        session = HTMLSession()
        new_url = URL_PAGS + str(i)
        print(new_url)
        print("----------------SCRAPEANDO PAGINA: {}-----------------------".format(i))
        response = session.get("{}".format(new_url), headers = headers)
        # all_urls = []
        all_urls = response.html.xpath(xpath_url)
        """ print(all_urls) """
        # for url in all_urls:
        #     # L_url.append(url)
        #     print(url)
            # cur.execute("DELETE FROM noticia WHERE url = '" + url + "'")
            # obtenerDatosUrl(url);
    else:
        response = session.get("{}{}".format(URL_SEED, i), headers = headers)
        all_urls = response.html.xpath(xpath_url)
        """ print(all_urls) """
        # for url in all_urls:
        #     # L_url.append(url)
        #     print(url)
            # cur.execute("DELETE FROM noticia WHERE url = '" + url + "'")
            # obtenerDatosUrl(url);
    # time.sleep(2)
# print(len(all_urls))
for url in all_urls:
    print(url)
print(len(all_urls))
conn.commit() 
conn.close()