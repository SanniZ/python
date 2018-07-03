# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:07:18 2018

@author: Byng.Zeng
"""
import threading
import socket
#import time
#import os
from xml.parsers.expat import ParserCreate

class tcpFileTranferSAXParser(object):
    def __init__(self):
        self.__status = None
        self.__filename = None
        self.__buffer = ''
    
    def getData(self):
        return self.__buffer
        
    def getFilename(self):
        return self.__filename
    
    def startElement(self, name, attrs):
        #print('sax: start_element: %s, attrs: %s' % (name, attrs))
        if name == 'name':
            self.__status = 'StartName'
        elif name == 'data':
            self.__status = 'StartData'
        
    def endElement(self, name):
        #print('sax: end_element: %s' % name)
        if name == 'name':
            self.__status = None
        elif name == 'data':
            self.__status = None

    def charData(self, data):
        #print('sax: char_data: %s' % data)
        if self.__status == 'StartName':
            self.__filename = data
            #print('get  src: %s' % self.name)
        elif self.__status == 'StartData':
            self.__buffer += data
            #print('get  data: %s' % data)

class tcpFileTransferHost(object):
    def __init__(self, name='tcpFileTransferHost', addr=('127.0.0.1', 9999)):
        self.__name = name
        self.__addr = addr
        self.__fileName = None
        self.__data = None
        
    def getAddr(self):
        return self.__addr;

    def saveFile(self, filename, data, mode='a'):
        with open(filename, mode) as f:
            f.write(data)

    def tcplinkHandler(self, sock, addr):
        print("Accept new connect from %s:%s" % addr)
        sock.send(b'Welcome to tcpFileTransferHost!')
        data = ''
        while True:
            temp = sock.recv(1024)
            #time.sleep(1)
            
            if not temp:
                break
            else:
                data = data + temp

        print('recv data: %s' % data)
        
        # clear dataBuffer      
        
        # create saxParser to process data. 
        saxHdr = tcpFileTranferSAXParser()
        saxParser = ParserCreate()
        saxParser.StartElementHandler = saxHdr.startElement
        saxParser.EndElementHandler = saxHdr.endElement
        saxParser.CharacterDataHandler = saxHdr.charData
        saxParser.Parse(data)

        self.saveFile(saxHdr.getFilename(), saxHdr.getData())

        sock.close()
        print('Closed connection!')

    def startTcpServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print('bind: ', self.getAddr())
        s.bind(self.getAddr())
    
        s.listen(5)
    
        while True:
            print('Waitting for connect...')
            sock, addr = s.accept()
            print('accept %s:%s' % addr)
            t = threading.Thread(name='tcplinkHandler',
                                 target=self.tcplinkHandler,
                                 args=(sock, addr))
            t.start()

if __name__ == '__main__':    
    host = tcpFileTransferHost('server-ibm2012', ('127.0.0.1', 9999))
    host.startTcpServer()
