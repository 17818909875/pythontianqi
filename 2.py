import requests
#requests.ConnectionError网络异常，抛出异常再查，也可try except定义
#一般用try...except方法来爬虫
#通用框架
#r.raise_for_status()非200抛出错误
#r.encoding=r.apparent_encoding/utf-8 etc
#return r.text获取里面的数据
'''
try:
	kv={'user-agent':'Mozila/5.0'}
	r=requests.get('...',header=kv)
	r.status_code
	print(r.text)
except:
	print('xxxxx')
