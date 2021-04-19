#saving superstats in csv file

import requests
import json


with open('superstats.csv', 'w') as f:
    for i in range(1,11):
        link = f'https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}'
        r = requests.get(link)
        data = json.loads(r.text)
        text = ''
        for stats in data:
            text = stats['headline']
            text = text.replace(',', '')
            text = text.replace(' ', ',')
            f.write(text)
            f.write('\n')