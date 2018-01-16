import requests
from lxml import html
page = requests.get('http://www.spe.org/awards/regional-distinguished-achievement-award-petroleum-engineering-faculty.php')
tree = html.fromstring(page.content)
print(type(tree))



