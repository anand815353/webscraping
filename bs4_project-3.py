import requests
from bs4 import BeautifulSoup

link = f'https://www.imdb.com/chart/top/'
r = requests.get(link)
html = r.text
soup = BeautifulSoup(html , 'html.parser')
tbody = soup.find('tbody')
trs = tbody.find_all('tr')
with open('posts/imdb250.csv','w') as f:
    for tr in trs:
        name = tr.find('td', {'class':'titleColumn'})
        year = name.span
        rating = tr.find('td', {'class': 'ratingColumn imdbRating'})
        f.write("{},{},{}".format(name.a.text.replace(',',''),year.text.replace('(','').replace(')',''),rating.strong.text))
        f.write('\n')