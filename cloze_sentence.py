#from __future__ import unicode_literals, print_functions
import random
import spacy
nlp = spacy.load("en_core_web_sm")


doc = nlp("Apple is looking at buying U.K. startup in New York!")

#TODO get least freq ent

def noun_chunks(str):
    doc = nlp(str)
    chunks = []
    for chunk in doc.noun_chunks:
        chunks.append(chunk.text)
    return chunks

# randomly cloze out a chunk in sentence
def cloze_sent(str):
    chunks = noun_chunks(str)
    if len(chunks) == 0: return "ERR: No English noun in sentence"
    pos = random.randint(0, len(chunks)-1)
    cloze_chunk = chunks[pos]
    return str.replace(cloze_chunk, "___")

# return array of sentences from a text
def sents_break(str):
    nlp.add_pipe('sentencizer') 
    doc = nlp(str)
    sentences = [sent.text.strip() for sent in doc.sents]
    return sentences

# generate one quiz question
def get_quiz(sents):
    if len(sents) == 0: return "No quiz question can be generated."
    pos = random.randint(0, len(sents)-1) 
    return cloze_sent(sents[pos]),sents[pos]

#test = "Apple is looking at buying U.K. startup for $1 billion dollars in New York!"

# takes in string. return array of strings of entities
def ent_clumps(str):
    doc = nlp(str)
    clumps = []
    curr_type = None # keep track of current type
    prev_type = None
    curr_ent = '' # keep track of ent
    every_other = False

    for i in doc:
        if (i == doc[0]):
            curr_type = i.ent_type_
        if i.ent_type_:
            #if ent type is same as previous 
            print(i.ent_type_ , curr_type)
            if (i.ent_type_ == curr_type):
                curr_ent += i.text + ' '
                curr_type = i.ent_type_
            #if ent type is NOT same as previous 
            else:
                clumps.append(curr_ent[:-1])
                curr_ent = i.text + ' '
                curr_type = i.ent_type_
        else:
            curr_type = None

        if (i == doc[-1]):
            clumps.append(curr_ent[:-1])
        

    print(clumps)
    return

# cloze the first entity
def cloze_first_entity(doc):
    cloze_sent = []
    checked = True
    for tok in doc:
        text = tok.text
        if tok.ent_type_ and checked:
            text = tok.ent_type_
            text = "__"
            #print(text + ' ' + tok.ent_type_)
            checked = False
        cloze_sent += text + tok.whitespace_
    print("".join(cloze_sent))

    return
