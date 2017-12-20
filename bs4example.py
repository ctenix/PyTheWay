# -*- coding: utf-8 -*-

import urllib2

def download(url, user_agent=None):
    print 'Downloading:', url
    headers = {'User-agent': user_agent or 'wswp'}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
    return html
import re
url = 'http://127.0.0.1:8000/places/default/view/United-Kingdom-239'
html = download(url)
content = re.findall('<td class="w2p_fw">(.*?)</td>',html)
print content