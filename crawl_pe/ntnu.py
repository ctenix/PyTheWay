
from common import get_page
from common import tree
from common import save_list
url = "https://www.ntnu.edu/igp/employees"
page = get_page(url)
tree = tree(page)

scholars = tree.cssselect('.employeeInfo')
n = len(scholars)
info = []
for scholar in scholars:
    info.append(scholar.text_content())
#print(info)
#print("\n")
print(info[0])
save_list(info)









