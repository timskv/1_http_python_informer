#!/usr/bin/env python
import cgi
import Cookie
import os
import platform
from datetime import timedelta
from subprocess import Popen, PIPE




#form = cgi.FieldStorage()
#a = form["s1"].value
#c = Cookie.SmartCookie()
#c["st1"] = a
print "Content-Type: text/html"
#print c.output()
print

print '<html>'
print '<body>'

print 'Hello Yury'
print platform.platform()

print 'Python Version:'
print platform.python_version()


print 'ololo'
print os.listdir("/lib/modules")


with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(timedelta(seconds = uptime_seconds))

print uptime_string
 
meminf = Popen('cat /proc/meminfo', stdout=PIPE).communicate()
print meminf

#print '<pre>'
#print a
#print '</pre>'
#print '<form name="f2" action="2.py">'
#print '<input type="text" name="s2" size="15" />'
#print '<input type="Submit" value="Go!" />'
#print '</form>'
print '</body>'
print '</html>'
