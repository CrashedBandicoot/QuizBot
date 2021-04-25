import spacy
nlp = spacy.load("en_core_web_sm")


doc = nlp("Apple is looking at buying U.K. startup for $1 billion in New York!")

cloze_sent = []

for tok in doc:
    text = tok.text
    if tok.ent_type_:
        #text = tok.ent_type_
        text = "__"
    cloze_sent += text + tok.whitespace_

print("".join(cloze_sent))