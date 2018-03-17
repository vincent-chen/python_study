#!/usr/bin/python
#coding:utf-8

import time
import psutil
import urllib2
import pdb

while True:
  data=psutil.cpu_times()
  datadict={"usertime":str(data.user),
             "systemtime":str(data.system),
             "waitIo":str(data.iowait),
              "idle":str(data.idle)}

  strData="?%s=%s&%s=%s&%s=%s&%s=%s"
  urlData=strData%("usertime",data.user,"systemtime",data.system,"waitIo",data.iowait,"idle",data.idle)
  
  url="http://localhost:8000/cgi-bin/index.py"+urlData
  print urllib2.urlopen(url).read()
  time.sleep(5)
  
