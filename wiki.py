import wikipediaapi
import spacy
nlp = spacy.load("en_core_web_sm")


# section summary
def sect_summ (sections, level=0):
    for s in sections:
        print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
        print_sections(s.sections, level + 1)


# takes in page title, gives full text of page
# return tuple [0] = title, [1] = summary
def extract_page(title):
    wk = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    page_py = wk.page(title)

    #t("Page - Title: %s" % page_py.title)
    #print("Page - Summary: %s" % page_py.text)
    return page_py.title, page_py.text


#print title
print(extract_page('Python_(programming_language)')[0])