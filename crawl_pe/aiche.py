
from common import get_page
from common import tree
from common import save_list
url = "https://www.aiche.org/community/awards/winners/28951"
page = get_page(url)
tree = tree(page)

scholars = tree.cssselect('.field-content')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(scholar.text_content())
#print(info)
#print("\n")
print(info[0])
save_list(info)









