#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'hello, world'

name = raw_input('请输入你的年龄: ')
print name
name = int(name)
if name >= 18:
    print 'hello,', name
else:
    print '未满18岁'
