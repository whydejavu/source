import requests
from bs4 import BeautifulSoup
#提取章节内容
def getNovelChapter(url):    
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    try:
        title = soup.select('.bookname h1')[0].text    
        return title + '\n    ' + '\n    '.join(a for a in soup.select('#content')[0].text.split())
    except IndexError:
        return ''


url = 'http://www.biquge.tw/0_52/'    #小说目录页的网址
headers = {'Host':'www.biquge.tw',
           'Connection':'keep-alive',
           'Cache-Control':'max-age=0',
          'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36'}
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
    
title=soup.select('#info')[0].h1.text    #小说名称提取
author=soup.select('#info')[0].p.text.strip()    #小说作者提取


file = open(title + '.text','w')    #保存文件
file.write(title)
file.write('\n' + author + '\n\n')
             
i = 0
l = int(len(soup.select('#list dd')))
while (i<l):
    ChapterUrl = url + soup.select('#list dd').a['href'].split('/')[-1]
    file.write(getNovelChapter(ChapterUrl) + '\n\n')
    i=i+1
file.close()
print('下载完成')