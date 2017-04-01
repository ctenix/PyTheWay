#__*__coding:utf-8__*__

import requests

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response Body:'
    print response.text

def use_params_requests():
    #构建请求参数
    params = ({'param1':'hello','param2':'world'})
    print 'Request Params:'
    print params
    #发送请求
    response = requests.get(URL_GET,params=params)
    #处理响应
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Status Code:'
    print response.status_code
    print '>>>>Reason:'
    print response.reason



if __name__== '__main__':
    print '>>>Use simple requests:'
    use_simple_requests()
    print ''
    print '>>>Use params requests:'
    use_params_requests()
