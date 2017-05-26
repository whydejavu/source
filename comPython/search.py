import os
from docutils.parsers.rst.directives import path

def search(kw,dir = os.path.abspath('.'),count=0):
    # count = count +1
    for i in os.listdir(dir):
        path = os.path.join(dir,i)
        # print count,path
        if i == "index.html":
            strs = path
            if(str.format(strs).__sizeof__()<110):
                print  path
        if os.path.isfile(path) and kw in i:
            pass
            # print 'file',path
        if os.path.isdir(path):
            # print count,'dir',path
            search(path, path,count)

if __name__ == '__main__':
    print 'search ',dir,' start'
    search('index.html','/Users/zhangqiankun/openstackVideo/Template')