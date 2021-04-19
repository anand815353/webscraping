# "author name" - "his quote" for 10 pages


import requests
qoutes = []
authors = []
for i in range(1,11):
    link = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(link)
    html = r.text
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            qoute = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            qoutes.append(qoute.strip())

        if '<small class="author"' in line:
            author = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>','')
            authors.append(author.strip())

with open('posts/author_quote.txt', 'a', encoding='utf-8') as f:
    for j in range(len(qoutes)):
        f.write(str(j+1) + ') ' + authors[j] + ' - ' + qoutes[j] + '\n')
