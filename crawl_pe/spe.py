
from common import get_page
from common import tree
from common import save_list
from lxml import html

url = "http://www.spe.org/awards/regional-distinguished-achievement-award-petroleum-engineering-faculty.php"
page = get_page(url)
tree = tree(page)

scholars = tree.cssselect('div.details.toggle-content.hidden > p')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(html.tostring(scholar))
#print(info)
#print("\n")
print(info[0])
save_list(info)









