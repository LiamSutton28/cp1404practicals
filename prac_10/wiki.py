"""Wikipedia introduction program"""
import wikipedia
from wikipedia import PageError, DisambiguationError

page_title = input("Page Title: ")
while page_title != "":
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.search(page_title))
    except PageError:
        print(f"Page id '{page_title}' does not match any pages. Try another id!")
    page_title = input("Page Title: ")
print("Thank you.")