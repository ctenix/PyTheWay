import pandas
import numpy
import requests
from lxml import html


# Get response content from url
def get_page(url):
    page = requests.get(url).content
    return page


def save_html(url):
    response = requests.get(url)
    with open('data.html', 'w') as file:
        file.write(response.text)


def tree(page):
    # type: (object) -> object
    return html.fromstring(page)


# save list in file by string method
def save_list2(data_list):
    file = open('data.txt', 'w')
    file.write(str(data_list))
    file.close()


# save list in file by lines
def save_list4(data_list):
    data_list = [line + '\n' for line in data_list]
    file = open('data.txt', 'w')
    file.writelines(data_list)
    file.close()


# UnicodeEncodeError: 'ascii' codec can't encode character u'\xf8' in position 19: ordinal not in range(128)
def save_list1(data_list):
    file = open('data.txt', 'w')
    for i in data_list:
        file.write(i + '\n')
    file.close()


def save_list3(data_list):
    file = open('data.txt', 'w')
    for item in data_list:
        print>>file, item
    file.close()

def save_list(data_list):
    pd=pandas.DataFrame(data_list)
    pd.to_csv("data.csv",encoding="utf-8")
