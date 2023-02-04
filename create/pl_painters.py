from bs4 import BeautifulSoup
import requests
import re
import json

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_links(url, selector, class_):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    items = doc.find_all(selector, class_=class_)
    items = ' '.join([str(elem) for elem in items])
    links = re.findall(r'(\/wiki\/)(\S*)(?=")', items)
    return [''.join(tup) for tup in links]

def full_links(list_of_links):
    return ['https://pl.wikipedia.org' + i for i in list_of_links]

url = 'https://pl.wikipedia.org/wiki/Kategoria:Polscy_malarze_(chronologia)'
painters_main = get_links(url, 'div', 'CategoryTreeItem')

pages_links = full_links(painters_main)

painters_names = []
for page in pages_links:
    names = get_links(page, 'div', 'mw-category-group')
    painters_names.append(names)

painters_names = [item for sublist in painters_names for item in sublist]
write_json(painters_names, 'pl_painters_names.json')

