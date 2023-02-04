import json
import re

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

with open('wiki/en_painters_links.json', 'r') as f:
    data = json.load(f)

links = []
for i in range(len(data)):
    try:
        # match only first link
        match = re.search(r"(?<=<li><a href=\")(.*?)((?=\" title)|(?=\" class))", data[i]['painter'])
        links.append(match.group(0))
    except:
        pass
print(len(links))

write_json(links, 'en_painters_names.json')