#!/usr/bin/python3
# encoding: utf-8
#Created on 2017年7月13日
#@author: jimmyue
from bs4 import BeautifulSoup
from urllib import request
import requests
import time
import re 
#爬虫目标网址
url='https://veaicle.com/wechat/car.php'
#解析网址内容
wb_date=requests.get(url)
soup=BeautifulSoup(wb_date.text,'lxml')
#匹配a标签下with-animation类
titles=soup.select('a.with-animation')
#遍历爬取车型图片
model={}
for title in titles:
	#获取车型名称
	model_name=title.get_text()[1:]
	#获取车型URL
	model_id=re.sub(r'\D', "", title.get('href'))
	model_url='https://pro.so.car/static/products/'+model_id+'.png'
	#保存图片
	try:
		r=requests.get(model_url)
		if r.status_code==200:
			request.urlretrieve(model_url, model_name+'.png')
			print('已保存: '+model_name,model_url)
	except requests.ConnectionError:
		print(model_name+' 图片地址异常！')
print('\n图片导出完毕！')


	
