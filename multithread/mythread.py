#!/usr/bin/python
from threading import Thread


class myThread(Thread):
  def __init__(self,threadName,a,b):
     Thread.__init__(self,name=threadName)
     self.a=a
     self.b=b
  def run(self):
     print 'a:%d,b:%d'%(self.a,self.b)

mythread=myThread("newThread",2,5)
mythread.start()	  
