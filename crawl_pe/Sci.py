
from common import get_page
from common import tree
from common import save_list
url = "http://www.casad.cas.cn/chnl/371/index.html"
page = get_page(url)
tree = tree(page)

scholars = tree.cssselect('#allNameBar > dd > span > a')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(scholar.text_content())
#print(info)
#print("\n")
print(info[0:10])
save_list(info)









