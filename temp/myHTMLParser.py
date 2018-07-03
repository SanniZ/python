# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:31:47 2018

@author: yingbin
"""

from html.parser import HTMLParser
#from html.entities import name2codepoint

class myHTMLParser(HTMLParser):
    def myStartTag(self, tag, attrs):
        print('<%s>' % tag)
        
    def myEndTag(self, tag, attrs):
        print('</%s>' % tag)
        
    def myStartEndTag(self, tag, attrs):
        print('<%s/>' % tag)
        
    def myData(self, data):
        print(data)
        
parser = myHTMLParser('/home/yingbin/Music/AudioPlayer.html')