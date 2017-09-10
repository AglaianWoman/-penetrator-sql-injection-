#!/usr/bin/env python 
import wget
import time
import sys
import httplib
import socket
import httplib2

toolbar_width = 80

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("loading...") 
    sys.stdout.flush()

sys.stdout.write("\n")

print 'wait please'

wget.download('https://github.com/hacktoolspack/-penetrator-sql-injection-/archive/master.zip')