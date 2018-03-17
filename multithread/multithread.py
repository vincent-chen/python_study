#!/usr/bin/python
#coding:utf-8

from time import sleep,ctime
import thread

def loop0():
  print "start loop0 at \n\t",ctime()
  sleep(4)
  print "loop0 done at \n\t",ctime()


def loop1():
  print "start loop1 at \n\t",ctime()
  sleep(2)
  print "loop1 done at \n\t",ctime()


def main():
  print "main start： \n\t",ctime()
  thread.start_new_thread(loop0,())
  thread.start_new_thread(loop1,())
  sleep(3)
  print "all_end \n\t",ctime()

if __name__=='__main__':
  main()
  
