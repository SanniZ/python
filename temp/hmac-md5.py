# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:31:32 2018

@author: yingbin
"""

import random, hmac

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), ).hexdigest()
    
class User(object):
    def __init__(self, name, pwd):
        self.name = name
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.pwd = hmac_md5(self.key, pwd)
    


db = {
    'mike' : User('mike', '123456'),
    'nike' : User('nike', '123abc'),
    'duncan' : User('duncan', 'du2015')
}

def login(name, pwd):
    usr = db[name]
    return usr.pwd == hmac_md5(usr.key, pwd)

if __name__ == '__main__':
    while True:
        opt=raw_input('Exit(y/n):')
        
        if opt == 'y':
            exit()
        else:
            name = raw_input('Please input name:')
            pwd = raw_input('Please input password:')
        
            print login(name, pwd)