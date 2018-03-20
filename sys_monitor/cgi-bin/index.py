#/usr/bin/python
#coding: utf-8
import 	cgi
import MySQLdb as sql

data=cgi.FieldStorage() #接收请求
if data.has_key('usertime'):
  value=data['usertime'].value
  print 'ok'
else:
  value='not found'

con=sql.connect(user='root',password='1qaz@WSX',db='cpu',host='localhost')
cur=con.cursor()
cur.execute("insert into cpu values('%d','%s');"%(1,value))
con.commit()
cur.close()
con.close()

touch  test
