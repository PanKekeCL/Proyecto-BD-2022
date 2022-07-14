import spacy
nlp = spacy.load("es_core_news_md")

text = """AQUI VAN LOS TEXTOS DE LAS NOTICIAS"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)