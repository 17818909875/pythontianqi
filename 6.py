import requests
import re
while True:
	b=input()
	url='http://m.ip138.com/ip.asp?ip='
	r=requests.get(url+b)
	r.encoding=r.apparent_encoding
	a=re.search(r'本站主数据：.*?<',r.text)

	print(r.text[a.span()[0]+6:a.span()[1]-1])