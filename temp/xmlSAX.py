# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:15:42 2018

@author: yingbin
"""

from xml.parsers.expat import ParserCreate

class SaxHandler(object):
    def startElement(self, name, attrs):
        print('sax: start_element: %s, attrs: %s' % (name, attrs))
        
    def endElement(self, name):
        print('sax: end_element: %s' % name)
    
    def charData(self, data):
        print('sax: char_data: %s' % data)
        
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
        
hdr = SaxHandler()
par = ParserCreate()
par.StartElementHandler = hdr.startElement
par.EndElementHandler = hdr.endElement
par.CharacterDataHandler = hdr.charData

par.Parse(xml)