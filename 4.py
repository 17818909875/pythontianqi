import requests
kv={'wd':'python'}
r=requests.get('http://www.baidu.com/s',params=kv)#?后面的都不用自己写
print(len(r.text))#可以先看看多长