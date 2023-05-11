import sys
import re
import random
import client
import datetime


class MyList(list):
    def get(self):
        try:
            return self.pop(0)
        except:
            return ''
            

class Log(object):
    def __init__(self):
        self.orgstdout = sys.stdout
        self.log = open("log.txt", "r")
        self.texts = self.log.read()

    def write(self, msg):
        self.log = open("log.txt", "r")
        self.texts = self.log.read()
        self.texts += msg
        self.orgstdout.write(msg)
        self.log = open("log.txt", "w")
        self.log.write(str(self.texts))
        self.log.close()
    


def check_code(__code, __args=()):
    __code = re.sub(r'input\([^()]*\)', 'input()', __code)
    if type(__args) not in [list, tuple]:
        __args = [__args, ]

    __code = f"args15fg5g7 = MyList({__args})\n" + __code
    
    __code = __code.replace('input()', 'args15fg5g7.get()')

    sys.stdout = Log()
    try:
        exec(__code) 
    except Exception as e:
        print(e)

