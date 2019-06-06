import requests
from pypinyin import lazy_pinyin
from lxml import etree
from bs4 import BeautifulSoup
import time
class find():
	def find(city):
		try:
			pin=''.join(lazy_pinyin(city))
			url='http://tianqi.hao123.com/'+pin+'.html'
			kv={'user-agent':'Mozila/5.0'}
			r=requests.get(url,headers=kv)
			r.encoding=r.apparent_encoding
			url2='http://tianqi.hao123.com/air/'+pin+'.html'
			r2=requests.get(url2,headers=kv)
			r2.encoding=r2.apparent_encoding
			page=etree.HTML(r.text,etree.HTMLParser())
			page2=etree.HTML(r2.text,etree.HTMLParser())
			data={}
			data['now_tmp']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/span[1]/text()')[0]
			data['line1']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/span/text()')#大哥，text肯定是本身没有的，要下属一个span才行
			data['line2']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/span/text()')
			data['tom_tmp']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/text()')
			data['tom_data']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/text()')[0].split('\xa0')[0:5:2]#\xa0本身就是一个字符串，就是应该这样来进行数组切片
			data['two_tmp']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/text()')
			data['two_data']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/text()')[0].split('\xa0')[0:5:2]
			hours=page.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/table/tr/th/text()')#tbody他不解析。。。就像当年那个json一样...
			hour_tmp=page.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/table/tr/td/text()')[3:][::3]
			hour_wea=page.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/table/tr/td/text()')[3:][1::3]
			hour_wind=page.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/table/tr/td/text()')[3:][2::3]
			data['air']=page.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/span/text()')[0]
			simple=page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/text()')
			simple2=page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/text()')
			tradi=page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/text()')
			tradi2=page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/text()')
			data['who']=page.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/span/text()')
			data['threeday']=[]
			for i in ['1','2','3']:
				a=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div['+i+']/div/text()')
				a[0]=a[0].replace('\xa0',' ')
				a[1]=a[1].replace('\xa0',' ')
				b=page.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div['+i+']/div/span/text()')[0]
				a.append(b)
				data['threeday'].append(a)
			data['live']=[]
			data['hour']=[]
			for i in range(6):
				data['live'].append([simple[i],tradi[i]])#只能append不能直接添加
			for i in range(4):
				data['live'].append([simple2[i],tradi2[i]])#只能append不能直接添加
			for i in range(8):
				data['hour'].append([hours[i],hour_tmp[i],hour_wea[i],hour_wind[i]])
			data['huan']=page2.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/text()')[0][0]#对于不给的，一般都是省一个div等，试试即可
			data['tip']=page2.xpath('/html/body/div[2]/div/div[1]/div[3]/text()')[0]

			return data
		except:
			return False
if __name__=='__main__':
	print('这是小鲁班的一个文件，你应该点另一个文件')
	time.sleep(1)