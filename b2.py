import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.baidu.com')
r.encoding=r.apparent_encoding
#print(r.text)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.head)
print(soup.head.contents)#获得儿子节点的一个列表,如单独的\n也是儿子节点的单独类型
print(soup.body.contents[1])#children获得遍历迭代
print()
print(soup.a.parent.name)#直接先辈字符串不迭代，.parents要迭代,还可以加.name来只打印标签
print(soup.div.next_sibling)#只有同一父节点才能构成子节点的平行遍历关系,平行标签可能出现在<xxx>之外,此外可以多次用.next_sibling.next_sibling,此外由于只检索第一个，故此法检索第二个时还有可能
#获得同名的标签
print(soup.a.previous_sibling)
print(soup.a.parent)#这个叫平行遍历，可以通过一个节点获得另外一个节点的信息

