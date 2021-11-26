import re

import spacy
nlp = spacy.load("en_core_web_sm")
doc=nlp("my friend Mary has worked at ZENSAR since 2009,Mary wants to book a flight from london to dallas")

for ent in doc.ents:
    print("{} : {}".format(ent.text,ent.label_))
