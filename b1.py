from bs4 import BeautifulSoup
import requests
r=requests.get('http://www.baidu.com')
r.encoding=r.apparent_encoding#不必写utf8,直接写这个即可
demo=r.text
#demo='http://www.baidu.com'不能是url,要是直接是html文本
soup=BeautifulSoup(demo,'html.parser')#以html来解析
print(soup.prettify())#打印解析结果
print(soup.title,soup.a)#所有这种tag都可以这样做，返回第一个，正则都不用了...
print(soup.a.parent.name)
print(soup.a.attrs,soup.a.attrs['href'])#获得空字典而不会是none
print(soup.a.string)#直接获取标签里面的内容,里面的标签也被去掉了，但是他的注释除去<!--里面的字符也会被输出，可以通过type来过滤，和非注释是不同的