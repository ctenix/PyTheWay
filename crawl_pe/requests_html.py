import requests
from lxml import html
page = requests.get('https://www.aiche.org/community/awards/winners/28951')
tree = html.fromstring(page.content)
print(type(tree))



