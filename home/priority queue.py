#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:47:00 2017

@author: wyq
"""

import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print "Starting " + self.name
      process_data(self.name, self.q)
      print "Exiting " + self.name
#将对queue的操作作为原子操作 lock之间
def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
        data = q.get()
        queueLock.release()
        print "%s processing %s" % (threadName, data)
      else:
          queueLock.release()
      time.sleep(1)#如果没有sleep等待其他的thread打印，则打印数据乱序、thread退出也乱序；但是thread开始是有序的
      #有了，退出仍是乱序，打印和开始是穿插的，打印部分也可能是乱序（还是乱序）
      
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)#长度为10 的共享队列
threads = []
threadID = 1
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()# 开始运行
   threads.append(thread)
   threadID += 1


# 相当于queue.join()
while not workQueue.empty():
   pass

#通知thread停止 （当队列为空时候）
exitFlag = 1

for t in threads:
   t.join()
print "Exiting Main Thread"