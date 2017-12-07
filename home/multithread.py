#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:14:32 2017

@author: wyq
"""

import json
import logging
import os
import threading
import time


logger = logging.getLogger(__name__)

class mythread(threading.Thread):
    def __init__(self, threadID,name,counter):
        threading.Thread.__init__(self)
        self.name = name
        self.threadID  = threadID
        self.counter = counter
    
    def print_time(self,name,delay, counter):
        while counter:
            time.sleep(delay)
            print "%s: %s" % (name, time.ctime(time.time()))
            counter-=1
        
    def run(self):
        print "Starting " + self.name
        
        lock.acquire()
        self.print_time(self.name, self.counter, 3)        
        lock.release()
        
    
   
t = []

lock = threading.Lock()
  
t1= mythread(1, 'thread1',3)
t2= mythread(2, 'thread2',3)
t.append(t1)
t.append(t2)

for i in t:
    i.start()
    i.join()
    
print "Exiting Main Thread"           