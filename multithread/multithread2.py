#!/usr/bin/python
#coding:utf-8
from time import sleep,ctime
import thread

loops=[4,2]  #休眠时间
def loop(nloop,nsec,lock):
  print u"开始 \n\t",ctime()
  sleep(nsec)
  print u"loop \n\t",ctime()
  lock.release()

def loop2():
  print u"loop2 开始 \n\t",ctime()
  locks=[]
  nloops=range(len(loops))
  for i in nloops:
     lock=thread.allocate()
     lock.acquire()
     locks.append(lock)
  for i in nloops:
     thread.start_new_thread(loop,(i,loops[i],locks[i]))
#  sleep(5)
  print "all_done \n\t",ctime()

loop2()
