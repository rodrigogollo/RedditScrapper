from bs4 import BeautifulSoup
import requests
from os.path import basename
from requests_html import HTMLSession

url = "https://www.reddit.com/r/greentext/"

s = HTMLSession()
response = s.get(url)
response.html.render()


# page = requests.get(url)

soup = BeautifulSoup(response, features="html.parser")
articles = soup.find_all('article')

for idx, article in enumerate(articles):
    print(article.a.text)
    img = article.find('img')
    if img:
        src = img['src']
        print(src)
        f = open(basename(str(idx)+'.jpeg'), "wb")
        f.write(requests.get(src).content)
