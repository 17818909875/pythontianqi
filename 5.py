import requests
import os
url='https://gss3.bdstatic.com/-Po3dS\
ag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=4a2a5d67566034a83defb0d3aa7a2231/c8177f3e6709c93da3c0da91953df8dcd10054a2.jpg'
root='./'#不同于node,这格式要加/的
#if not os.path.exists(root) os.mkdir(root) 
path=root+url.split('/')[-1]

r=requests.get(url)
#print(r.status_code)
with open(path,'wb') as f:
	f.write(r.content)#图片视频音乐都可以爬
	