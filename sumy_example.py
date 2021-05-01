from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from cloze_sentence import cloze_sent,sents_break,get_quiz




def get_html_summ(url):
    LANGUAGE = "english"
    SENTENCES_COUNT = 10
    if __name__ == "__main__":
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        
        txt = ""
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            txt += sentence._text
            #TODO convert sentence to string
            #print(dir(sentence))
        return txt

#url = "https://realpython.com/beautiful-soup-web-scraper-python/"
#print(get_html_summ(url))

def summ_from_inp():
    inp = input("Enter your link: ")
    summ = get_html_summ(inp)
    sentences = sents_break(summ)
    quiz = get_quiz(sentences)
    print(summ)

    while True: 
        inp = input("Commands: q - give quiz quesiton, r - reveal answer, a - another quiz, e - exit: " )
        if inp == "q":
            print(quiz[0])
        elif inp == "r":
            print(quiz[1])
        elif inp == "a":
            quiz = get_quiz(sentences)       
            print(quiz[0])
        elif inp == "e":
            return
        else:
            print("Invalid command.")
        
summ_from_inp()