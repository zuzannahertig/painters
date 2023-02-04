import json
import requests
import sqlite3
import os

def write_json(data, filename):
    with open('data/' + filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_response(name, language):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'accept': 'application/json'}
    response = requests.get(
        f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{language}.wikipedia.org/all-access/user/{name}/monthly/20220101/20230101',
        headers=headers,
    )
    data = response.json()
    write_json(data, filename=f'{name}.json')

def read_data_from_json(json_file):
    with open(f'{json_file}', 'r') as f:
        projects = []
        articles = []
        granularities = []
        timestamps = []
        accesses = []
        agents = []
        views = []
        try:
            data = json.load(f)
            data = data['items']

            for e, i in enumerate(data):
                projects.append(data[e]['project'])
                articles.append(data[e]['article'])
                granularities.append(data[e]['granularity'])
                timestamps.append(data[e]['timestamp'])
                accesses.append(data[e]['access'])
                agents.append(data[e]['agent'])
                views.append(data[e]['views'])
        except:
            pass
    
    return projects, articles, granularities, timestamps, accesses, agents, views

def get_views_data(filename, language):
    with open(f'{filename}', 'r') as f:
        data = json.load(f)
    names = [i[6:] for i in data]
    
    for name in names:
        get_response(name, language=language)

get_views_data('en_painters_names.json', 'en')
get_views_data('pl_painters_names.json', 'pl')

conn = sqlite3.connect('painters.db')
c = conn.cursor()
# c.execute(''' DROP TABLE painters ''')
c.execute('''CREATE TABLE IF NOT EXISTS 
painters(project TEXT, article TEXT, granularity TEXT, timestamp TEXT, access TEXT, agent TEXT, views INT)''')

directory = './data/'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    projects, articles, granularities, timestamps, accesses, agents, views = read_data_from_json(f)

    for i in range(len(projects)):
        c.execute('''INSERT INTO painters VALUES(?,?,?,?,?,?,?)''', (projects[i], articles[i], granularities[i], timestamps[i], accesses[i], agents[i], views[i]))
        conn.commit()

c.execute(''' SELECT project FROM painters ''')
results = c.fetchall()
print(results)

conn.close()