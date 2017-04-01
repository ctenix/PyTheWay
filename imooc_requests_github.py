# -*- coding:utf-8 -*-
import json
import requests
URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str),indent = 4)

def requests_method():
    response = requests.get(build_uri('user/emails'), auth=('user','passwd'))
    print better_print(response.text)

if __name__ == '__main__':
    requests_method()
