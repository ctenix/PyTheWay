
from common import get_page
from common import tree
from common import save_list
url = "http://www.cae.cn/cae/html/main/col48/column_48_1.html"
page = get_page(url)
tree = tree(page)

scholars = tree.cssselect('.name_list>a')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(scholar.text_content())
#print(info)
#print("\n")
print(info[0])
save_list(info)









