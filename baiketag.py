import urllib2
import urllib
import requests
##import json
##import time

headers={
	'Connection': 'keep-alive',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	"Origin": "http'://baike.baidu.com",
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': "http://baike.baidu.com/wikitag/taglist?tagId=68036",
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	'Cookie': 'BAIDUID=1F7661DA76752617F88264175D1511F5:FG=1; BIDUPSID=1F7661DA76752617F88264175D1511F5; __cfduid=d626a622e17b351459497fdf8bdd112fd1485458229; pgv_pvi=3655767040',
	}

url="http://baike.baidu.com/wikitag/api/getlemmas"
s=requests.session()
data={
	'limit':'24',
	'timeout':'3000',
	'filterTags':'[]',
	'tagId':'68036',
	'fromLemma':'false',
	'contentLength':'40',
	'page':'0',
	}

t=s.post(url,headers=headers,data=data).text
print t
