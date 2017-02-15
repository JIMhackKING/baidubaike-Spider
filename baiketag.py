#coding:cp936

"""�ٶȰٿƷ��������������
�ó�����ݸ�����tagId��������ȡ�ٶȰٿƴ�������ҳ�棬
���ѽ�����浽�ļ��У�
�ó���û����Ϊģ�鵼��ı�Ҫ"""

__auther__='JIMhackKING'

import urllib2
import urllib
import requests
import json

#��װ����Ϊһ����
class Spider(object):

    def __init__(self,tagId):
        self.tagId=tagId
        #����headers
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

        #�ٿƷ��������url�����󷽷�ΪPOST
        self.url="http://baike.baidu.com/wikitag/api/getlemmas"

    #��ҳ��������������ʵ���صľ���һ��json
    def parser(self):
        #�����Ự������cookie��
        s=requests.session()

        #ҳ��ѭ��
        for num in range(100):
            #����Post����
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
            #�����д���ļ�
            f=open('citiao.txt','a+')
            #��ȡ�ļ��ڵĴ�������ֹ�����ظ�
            entrys=f.readlines()
            #��responseת��Ϊjson���з�������ô���������
            for params in json.loads(t,encoding='utf-8')[u'lemmaList']:
                param = params[u"lemmaCroppedTitle"]
                print (param)
                if param.encode('utf-8') not in entrys:
                    f.write(param.encode('utf-8')+'\n')
            f.close()
            
            
if __name__ == '__main__':
    import sys
    tagId=raw_input("tagId:")
    #����python�汾�任���뺯��
    if sys.version_info[0] is '2':
        spider=Spider(tagId)
    else:
        spider=Spider(tagId)
    spider.parser()
else:
    print ("�ٶȰٿ�����ɹ�����(*^__^*)")
