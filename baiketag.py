#coding:cp936

"""百度百科分类词条名的爬虫
该程序根据给出的tagId参数来爬取百度百科词条分类页面，
并把结果保存到文件中，
该程序没有作为模块导入的必要"""

__auther__='JIMhackKING'

import urllib2
import urllib
import requests
import json

#封装爬虫为一个类
class Spider(object):

    def __init__(self,tagId):
        self.tagId=tagId
        #设置headers
        self.headers={
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                "Origin": "http'://baike.baidu.com",
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': "http://baike.baidu.com/wikitag/taglist?"+tagId,
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cookie': 'BAIDUID=1F7661DA76752617F88264175D1511F5:FG=1; BIDUPSID=1F7661DA76752617F88264175D1511F5; __cfduid=d626a622e17b351459497fdf8bdd112fd1485458229; pgv_pvi=3655767040',
                }

        #百科分类词条的url，请求方法为POST
        self.url="http://baike.baidu.com/wikitag/api/getlemmas"

    #网页分析主函数，其实返回的就是一个json
    def parser(self):
        #创建会话（保持cookie）
        s=requests.session()

        #页码循环
        for num in range(100):
            #设置Post参数
            data={
                    'limit':'24',
                    'timeout':'3000',
                    'filterTags':'[]',
                    'tagId':self.tagId,
                    'fromLemma':'false',
                    'contentLength':'40',
                    'page':num,
                    }

            t=s.post(self.url,headers=self.headers,data=data).text
            #将结果写进文件
            f=open('citiao.txt','a+')
            #获取文件内的词条，防止词条重复
            entrys=f.readlines()
            #将response转换为json进行分析，获得词条的名称
            for params in json.loads(t,encoding='utf-8')[u'lemmaList']:
                param = params[u"lemmaCroppedTitle"]
                print (param)
                if param.encode('utf-8') not in entrys:
                    f.write(param.encode('utf-8')+'\n')
            f.close()
            
            
if __name__ == '__main__':
    import sys
    tagId=raw_input("tagId:")
    #根据python版本变换输入函数
    if sys.version_info[0] is '2':
        spider=Spider(tagId)
    else:
        spider=Spider(tagId)
    spider.parser()
else:
    print ("百度百科爬虫成功导入(*^__^*)")
