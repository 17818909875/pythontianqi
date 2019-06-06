import requests
r=requests.get('http://www.baidu.com')
r.encoding=r.apparent_encoding
demo=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser')#会自动转换utf-8,并没有障碍
print(soup.prettify())#加了换行符缩进等更加清晰了,用来解析文档
print(soup.a.prettify())#tag name attribute...都可以拿到  