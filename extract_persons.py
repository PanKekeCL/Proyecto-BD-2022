import spacy
nlp = spacy.load("es_core_news_md")

# MI IDEA
# Utilizando el cuerpo de una Noticia, se recorre.
# Se busca todas las palabras que empiezen con mayuscula y esten decorrido. EJ: Los actores Dwayne Johnson y Kevin Hart son...
# Esas palabra [Los, Dwayn Johnson, Kevin Hart] se guardan en una lista. Se encuentran varias hasta recorrer todo el texto.
# Luego se busca en la api dewikipedia, si existe y dice que es una persona, se valida.
# Esto podria entregar una lista de personas mencionadas.

text = """AQUI VAN LOS TEXTOS DE LAS NOTICIAS"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)