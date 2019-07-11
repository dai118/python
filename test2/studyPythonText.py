#!/usr/bin/python
# -*- coding:utf8 -*-

class ShortInputClass:
    def __init__(self,length, atlast):
        Exception.__init__(self)
        self.length = length
        self.atlast = atlast

try:
    text = input('enter text:')
    if len(text) < 3:
        ShortInputClass(len(text),3)
except EOFError:
    print('why do you give me a eof?')
except ShortInputClass as ex:
    print('your text {0} long,and except at least{1}'.format(ex.length, ex.atlast))
else:
    print('no except')




