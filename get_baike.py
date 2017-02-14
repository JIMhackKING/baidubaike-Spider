#-*-decoding:UTF-8-*-
import re
import requests as rq
from bs4 import BeautifulSoup
import os
import time
##import urllib,urllib2
import random

#爬虫主函数
def get_baidubaike(keyword):
    url = 'http://baike.baidu.com/item/{}'.format(keyword)
    html = rq.get(url).content
    
    #urllib2可以忽略字符串的换行符
    #html=urllib2.urlopen(url).read()

    #匹配content属性的标签
    regex = re.compile('content="(.*?)">')
    words = re.findall(regex, html)[0]

    #用BeautifulSoup解析文档树
    soup=BeautifulSoup(html,'html5lib')
    tag=soup.find('div',class_="lemma-summary")
    summarys=tag.find_all('div')
    #把树形结构的字符结合起来
    summary=''
    for texts in summarys:
        text=texts.text
        summary += re.sub(r'\[\d\]','',text)

    
    return summary,words

if __name__ == '__main__':
    fp=open("citiao.txt")
    if not os.path.exists("baike"):
        os.mkdir("baike")
    os.chdir("baike")
    for f in fp.readlines():
        summary,words = get_baidubaike(f.strip())
##        print type(summary),type(words)
        with open("%s.txt" %(f.strip().decode('utf-8')),'w') as fs:
            fs.write(words+'\n'+summary.encode('utf-8')+'\n')  #待测试，bytes(bytearray(html, encoding='utf-8'))函数转化为bytes型数据
        print (words)
        print
        print (summary)
        time.sleep(5+random.random()*5)
    fp.close()
##    summary,words = get_baidubaike(raw_input("what do you want to search?"))
##    print (words)
##    print
##    print (summary)
        
    

        
