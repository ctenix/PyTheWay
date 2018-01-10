from common import tree
from common import save_list
path = './hgd.html'
with open(path,"r") as page:
    tree = tree(page)
    scholars = tree.cssselect('.br')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(scholar.text_content())
#print(info)
#print("\n")
print(info[0])
#save_list(info)









