import requests
from bs4 import BeautifulSoup
from pypinyin import lazy_pinyin
url='http://toy1.weather.com.cn/search?cityname='
city='广州'
pin=''.join(lazy_pinyin(city))
url+=pin
kv={'user-agent':'Mozila/5.0'}
r=requests.get(url,headers=kv)
print('first ok')
url='http://www.weather.com.cn/weather1d/'+r.text[10:19]+'.shtml'
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
print(soup.select('.t'))
#today > div.t > div > p.time > span
#page=etree.HTML(r.text,etree.HTMLParser())
#print(page)
#up_time='/*div[2]/div/p[1]/span/text()'#怎么还是找不到啊
#print(page.xpath(up_time))
#中国天气网好贱，不爬他了