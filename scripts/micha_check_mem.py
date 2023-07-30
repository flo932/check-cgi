#!/usr/bin/env python3
import sys
"""
https://community.icinga.com/t/add-custom-service-check-with-python-script/4703/3

object CheckCommand "python-script1" {
   command = [ PluginDir + "/check_micha" ]

   arguments = {
      "-s" = "$address$"
      "-q" = "$db_server$"
      "-u" = "$db_username$"
      "-p" = "$db_password$"
      "-c" = "check_mem.cgi"
   }
}
object Host "deb8-fertigung-micha" {
#import "generic-host"
address = "192.168.0.28"
check_command = "python-script1"
}
"""
import time
import os
from collections import OrderedDict

import hashlib
import time

import micha_token as token

if "-psk" in sys.argv:
    i = sys.argv.index("-psk")
    _tmp=sys.argv[i+1]
    tt = _tmp
    t = token.token(tt)
else:
    t = token.token()


x=os.environ
x=dict(x)
x= sys.argv

print( sys.argv )
_exit = 100

try:
    h="192.168.0.28"
    if "-a" in sys.argv:
        i = sys.argv.index("-a")
        _h=sys.argv[i+1]
        #if _h.endswith(".de"):
        #    h= _h
        h = _h
    else:
        _exit = 4
        print("-a ip not set !") 
        print("exit:",_exit)
        sys.exit(_exit)

    cmd="curl http://{}:/sys/check_mem.cgi?token={}".format(h,t)
    cmd += " 2> /dev/null"
    print(cmd)
    x=os.popen(cmd)
    #print(x)
    print("----response----")
    for line in x.readlines():
        line = line.strip()
        print(line)

        if line.startswith("exit:"):
            #print("<--->")
            try:
                _exit = int(line.split(":")[-1])
                print("<--->",_exit)
                print()
            except Exception as e:
                print("_exit",e)

finally:
    pass
sys.exit(_exit)
