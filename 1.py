import requests
r=requests.get('http://www.baidu.com',params=None)#与post相同去爬取信息，但是正则好难,这里构造请求request,None可以是字典或则字节流,r此时是response对象
r.encoding='utf-8'#可以用r.apprent_encoding时猜测的编码方式,如果header不存在charset,就不能解析中文了，如百度，注意header不是head，所以百度没有
print(r.text)#字符串形式信息
#r.content,http响应内容的二进制形式，如图片就是这种形式