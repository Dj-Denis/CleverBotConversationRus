# -*- coding: utf-8 -*-
# encoding=utf8
from cleverbot import Cleverbot
import time
import pyttsx
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

en = pyttsx.init()

cb1 = Cleverbot()
cb2 = Cleverbot()

s = cb1.ask('Привет')
while True:
    print('bot1> ' + s)
    en.say(s)
    en.runAndWait()
    s = cb2.ask(s)
    print('bot2> ' + s)
    en.say(s)
    en.runAndWait()
    time.sleep(1)
    s = cb1.ask(s)
    time.sleep(1)
