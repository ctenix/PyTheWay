import requests
from lxml import html
page = requests.get('http://www.lsu.edu/eng/pete/people/faculty/index.php')
tree = html.fromstring(page.content)
print type(tree)



