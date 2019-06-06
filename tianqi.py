import requests
from lxml import etree
r=requests.get('https://tianqi.moji.com/weather/china/guangdong/foshan')
r.encoding=r.apparent_encoding
page=etree.HTML(r.text,etree.HTMLParser())#此时可以开始用xpath了
#result=etree.tostring(page)
#print(result)
print(page.xpath('/html/body/div[4]/div[1]/div[2]/em/text()'))#当前温度
#对不起，xpath就是要直接做手脚，不然直接只返回一个对象,到要到的地方加/t
print(page.xpath('/html/body/div[4]/div[1]/div[2]/b/text()'))
