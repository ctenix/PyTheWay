
from common import get_page
from common import tree
from common import save_list
url = "http://www.spe.org/awards/regional-distinguished-achievement-award-petroleum-engineering-faculty.php"
page = get_page(url)
tree = tree(page)

scholars = tree.cssselect('div.details toggle-content hidden > p > strong')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(scholar.text_content())
#print(info)
#print("\n")
print(info[0])
#save_list(info)









