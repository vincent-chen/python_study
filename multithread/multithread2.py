#!/usr/bin/python
#coding:utf-8
from time import sleep,ctime
import thread
from multiprocessing import Process,Lock
import pdb
import os

def sub_pro(l,num):
  l.acquire()
  print os.getpid(),'has',num
  l.release()


if __name__=="__main__":
#def main():
  lock=Lock()
  for i in range(10):
    p=Process(target=sub_pro,args=(lock,i))
    p.start()
    p.join()

#if "__name__"=="__main__":
#  main()
