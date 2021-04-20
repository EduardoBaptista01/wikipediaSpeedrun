
import requests
from bs4 import BeautifulSoup

res = requests.get(f"https://en.wikipedia.org/wiki/Gondomar,_Portugal").text

soup = BeautifulSoup(res, 'html.parser')

print(soup.bodyContent.prettify())

no_wants = ['/w/', 'File:', 'Category:', 'Template:', 'Help:', 'Wikipedia:', 'Special:']

links = []

for link in soup.body.find_all('a'):
    # print(link.get('href'))
    links.append(link.get('href'))

len_link1 = len(links)
links2 = []
for link in links:
    if str(link)[0:6] != '/wiki/' or\
            '/w/' in str(link) or\
            '/wiki/File:' in str(link) or\
            '/wiki/Category:' in str(link) or\
            '/wiki/Template:' in str(link) or\
            '/wiki/Help:' in str(link) or \
            '/wiki/Portal:' in str(link) or \
            '/wiki/Wikipedia:' in str(link) or \
            '/wiki/Talk:' in str(link) or \
            '/wiki/Special:' in str(link):
        continue
    links2.append(str(link))

len_link2 = len(links)

print(links2)
print(f"{len_link2} / {len_link1}")

