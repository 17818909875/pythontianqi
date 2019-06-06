from e3 import find#不是一个包，不能直接把包里面的函数引入，但可以直接引入文件再用类
import time
def  welc():
	print('=====================提示==================')
	print('这是鲁班七号制作的一个爬虫，爬取hao123天气网的数据并渲染到这里，免去了看广告,如果网页结构不变，则一直可以使用哦，而且是免费的哦')
	print('制作者：黄黄的可爱的鲁班七号')
	print('请输入你要爬取的中国城市，不输入(输入字符为空)则退出程序，按回车结束')
	city=input()#回车是不会被读进去的，要不什么都判断不了了
	return city
def find_city(city):
	print('小鲁班正在查找数据，大概要几秒钟哦，请确保你的网络是通畅的')
	data=find.find(city)
	print('====================天气信息====================')
	if  data==False:
		print('你输入的城市名解析不出来呢，要么是网页结构发生了变化，这个不能用了呢')
	else:
		print('当前查询城市：'+data['who'][1]+'   查询时间: '+data['who'][0])
		print('当前温度: '+data['now_tmp']+'℃   当前湿度: '+data['line2'][2][2:]+'%   当前天气:'+data['line1'][0])
		tem=data['threeday'][0][0].split(' ')
		con=data['line1'][1][4:]
		print('今天天气: '+tem[2]+'-'+tem[4]+'   空气质量:'+con+'   pm2.5: '+data['line2'][0][5:]+'   气压:'+str((int(data['line2'][1][2:]))/10)+'kPa')#真的整形该转还是转了
		print('明天温度:'+data['tom_tmp'][0]+'℃   天气:'+data['tom_data'][0]+'   风力:'+data['tom_data'][1]+'   空气质量:'+data['tom_data'][2][4:])
		print('后天温度:'+data['two_tmp'][0]+'℃   天气:'+data['two_data'][0]+'   风力:'+data['two_data'][1]+'   空气质量:'+data['two_data'][2][4:])
		print('================================================')
		print('3小时间隔详细播报:')
		for i in data['hour']:
			print('时间:'+i[0]+'   温度:'+i[1]+'   天气：'+i[2]+'   风力:'+i[3])
		print('==============================================')
		print('生活指数:')
		j=0
		for i in data['live']:
			j+=1
			print(i[0],end='   ')
			if j%3==0:
				print()
		print()
		print('提示:'+data['tip'])
city=welc()#这种结构怎么快那么多?
while True:
	if city=='':
		break
	find_city(city)
	time.sleep(1)
	city=welc()
print('欢迎再次使用小鲁班制作的天气爬虫工具哦')
time.sleep(1)#1s