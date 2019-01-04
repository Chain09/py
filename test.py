#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

index = 0
log = open('C:\\Users\\hspcadmin\\Desktop\py\\2018-11-27-bar_ufx-mainsvr-0--1.log')
try:
    for line in log:
        lineD = line.decode('GB2312')
        found = re.search('转发错误'.decode('UTF-8'), lineD)
        if found != None:
            index = index + 1
            print lineD
            if index == 100:
                print '100 records has been done.'
    print 'job done!'
except Exception as e:
    print e
    pass
