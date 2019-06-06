import requests
import json
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'#_0不给我怕？！
data={}
data['doctype'] ='json'
while True:
	content=input('请输入需要的英文或中文:\n')
	data['i'] = content
	response=requests.post(url,data=data)#打包了
	response.encoding='utf-8'
	print(content,'==>',json.loads(response.text)['translateResult'][0][0]['tgt'])