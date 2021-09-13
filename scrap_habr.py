import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']


URI = 'https://habr.com'
response = requests.get(f'{URI}/ru/all/')


soup = BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    title = article.find('h2').find('a')
    link = title.attrs.get('href')
    URL = f'{URI}{link}'
    resp = requests.get(URL)
    s = BeautifulSoup(resp.text, features='html.parser')
    entire_article = s.find_all('div', class_='tm-page-article__body')
    for a in entire_article:
        for keyword in KEYWORDS:
            if keyword in a.text or keyword.capitalize() in a.text:
                datetime = s.find('time').attrs.get('title')
                date = datetime.split(', ')[0]
                title = s.find('h1', class_='tm-article-snippet__title tm-article-snippet__title_h1')
                print(f'{date} - {title.text} - {URL}')
                break
