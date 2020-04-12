# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

def load():
    load = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in nuke:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)
        
load()
