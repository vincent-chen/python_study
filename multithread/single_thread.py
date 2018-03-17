#coding:utf-8

from time import sleep,ctime
import thread

def loop0():
  print u"第一个函数1 \n\t",ctime()
  sleep(4)
  print u"第一个函数2 \n\t",ctime()

def loop1():
  print u"第二个函数1 \n\t",ctime()
  sleep(2)
  print u"第二个函数2 \n\t",ctime()
  

def main():
  print u"第三个函数1 \n\t",ctime()
  loop0()
  loop1()
  print u"第三个函数2 \n\t",ctime()
  
main()
