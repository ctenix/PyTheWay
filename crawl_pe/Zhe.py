
from common import get_page
from common import tree
from common import save_list
url = "http://che.zju.edu.cn/cn/redir.php?catalog_id=61439"
page = get_page(url)
tree = tree(page)

scholars = tree.cssselect('div.con > ul > li > a ')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(scholar.text_content())
#print(info)
#print("\n")
print(info[1])
save_list(info)









