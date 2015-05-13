__author__ = 'Candy'

import  urllib2
import urllib
import cookielib
"""response = urllib2.urlopen('http://www.baidu.com')
html = response.read()
print html
"""
#get cookies first
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
opener.open('http://www.zhihu.com')
print cookie
for item in cookie:
    print 'name='+item.name
    print 'value='+item.value

data={
    "email":"cindyrain@126.com",
    "password":"ty6450323521"
}
data = urllib.urlencode(data)
headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
print data
request = urllib2.Request('http://www.zhihu.com/login',data,headers,cookie)
response = urllib2.urlopen(request)
page = response.read()
print page