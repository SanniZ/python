# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:15:43 2018

@author: Byng.Zeng
"""

import socket

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

class tcpFileTransferClient(object):
    def __init__(self, name='tcpFileTransferClient', addr=('127.0.0.1', 9999)):
        self.name = name
        self.status = None
        self.addr = addr

    def transferFile(self, src, tgt):
        print("src: %s, target: %s" % (src, tgt))

        with open(src, 'r') as f:
            data = f.read()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect(self.addr)
        print('connect to %s:%s' % self.addr)
        
        print(sock.recv(1024))
        
        xml=r'''<?xml version="1.0"?>
            <xml>
                <name>%s</name>
                <data>%s</data>
            </xml>
            ''' % (tgt, data)
        sock.send(xml)      
        
        sock.close()

if __name__ == '__main__':
    client = tcpFileTransferClient('testTCPFileTransfer', ('127.0.0.1', 9999))
    client.transferFile('/home/yingbin/tcpSrcData.txt',
                        '/home/yingbin/revTcpData.txt')
