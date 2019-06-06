import requests
r=requests.get('http://www.baidu.com')
r.encoding=r.apparent_encoding
demo=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser')
print(soup.find_all('a',''))#可以查找所有a标签等,第二个是看属性值有没有与之符合的
'''print(soup.find_all(['a','p']))
for tag in soup.find_all(True):
	print(tag.name)#每个标签的name名字'''
print(soup.find_all(id='a'))#id可以但是class不行








