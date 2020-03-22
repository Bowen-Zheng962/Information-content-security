import requests
import bs4
import os
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)    #获取网页
		r.raise_for_status()    #获取网页的状态，判断是否发生
		r.encoding = r.apparent_encoding    #更改编码
		return r.text    #未出现错误返回文本
	except:
		return ""    #出现错误返回空字符串
	return ""

def fillUnivList(ulist , html):    #获取信息并填入列表
	soup =BeautifulSoup(html,"html.parser")    #进行HTML文件的解析
	for tr in soup.find ('tbody').children:    #遍历tbody的子结点
		if isinstance(tr,bs4.element.Tag):     #判断数据类型是否为Tag型
			tds =tr('td')                      #将td标签整合至tds列表中
			ulist.append([tds[0].string ,tds[1].string ,tds[2].string ])    #将网页信息填入列表中
	pass

def printUnivList(ulist, num):    #打印结果并创建文件写入
	path ="../result/排名.txt"    #定义路径
	tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"    #定义输出格式
	print (tplt.format("排名","学校名称","地区",chr(12288)))    #打印
	with open (path,'a') as f:                                 #进行文件创建与写入
		f.write(tplt.format("排名","学校名称","地区",chr(12288))+'\n')
	for i in range (num):                                      #遍历列表并采用格式化输出信息
		u=ulist[i]
		print (tplt.format(u[0],u[1],u[2],chr(12288)))
		with open (path,'a') as f:
			f.write(tplt.format(u[0],u[1],u[2],chr(12288))+'\n')

		
def main():
	uinfo=[]
	url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'    #目标网址（url）
	html=getHTMLText(url)    #获取目标url的信息
	fillUnivList(uinfo,html)    #将数据填入数据结构——列表中
	printUnivList(uinfo,100)    #打印、输出

main()