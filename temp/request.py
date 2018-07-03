# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:49:08 2018

@author: yingbin
"""

import urllib

try:
    with urllib.urlopen('www.baidu.com') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s - %s' % (k, v))
            
        print('Data:', data.decode('utf-8'))
except IOError as e:
    print('IOError: ', e)