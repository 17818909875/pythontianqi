import requests
url='http://www.taobao.com'
r=requests.get(url)#可以r.raise_for_status()，不必要200的if条件判断
#r.status_code这些都是以属性而不是方法来直接赋值来改的
print(r.encoding) #头部不必要先定义，如果头部有则这里已经会改
print(r.text[:50])