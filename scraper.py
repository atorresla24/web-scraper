import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_basketball#cite_note-James_Naismith-1"


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    list_items = soup.find_all("a", attrs={"title": "Wikipedia:Citation needed"})
    print("citations needed: ", len(list_items))


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    list_items = soup.find_all("a", attrs={"title": "Wikipedia:Citation needed"})
    for item in list_items:
        print(item.parent.parent.parent.text)


get_citations_needed_report(url)

get_citations_needed_count(url)
