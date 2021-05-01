from sumy_example import get_html_summ
from cloze_sentence import cloze_sent,sents_break,get_quiz


teststr = "Hello, world. Here are two sentences."
def summ_from_inp():
    #inp = input("Enter your link: ")
    summ = get_html_summ("https://realpython.com/beautiful-soup-web-scraper-python/")
    #print(get_quiz(sents_break("Hello, world. Here are two sentences.")))
    


summ_from_inp()