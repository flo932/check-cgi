#!/usr/bin/env python3
# 2022 GPL v2 only
# - flo932@uxsrv.de micha.r
import sys
"""
https://community.icinga.com/t/add-custom-service-check-with-python-script/4703/3

object CheckCommand "python-script1" {
   command = [ PluginDir + "/check_xxx" ]

   arguments = {
      "-s" = "$address$"
      "-q" = "$db_server$"
      "-u" = "$db_username$"
      "-p" = "$db_password$"
   }
}
object Host "deb8-fertigung-xxx" {
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


import xxx_token as token

if "-psk" in sys.argv:
    i = sys.argv.index("-psk")
    _tmp=sys.argv[i+1]
    tt = _tmp
    t = token.token(tt)
else:
    t = token.token()

_exit = 1000
x=os.environ
x=dict(x)
x= sys.argv
#f = open("/tmp/env.log","w")
#f.write(str(x))
#f.close()
print( sys.argv )

try:
    #cmd= "ps -Ao %cpu,command  | grep mysqld"
    #os.system(cmd)
    h="192.168.0.28"
    if "-a" in sys.argv:
        i = sys.argv.index("-a")
        _h=sys.argv[i+1]
        #if _h.endswith(".de"):
        #    h= _h
        h = _h
    m=""
    if "-m" in sys.argv:
        i = sys.argv.index("-m")
        _h=sys.argv[i+1]
        m = _h
    while ".." in m:
        m = m.replace("..","")
    while "/" in m:
        m = m.replace("/","")

    cmd="curl 'http://{}:/sys/check_mount.cgi?token={}&code={}'".format(h,t,m)
    cmd += " 2> /dev/null"
    print(cmd)
    x=os.popen(cmd)
    txt=x.read()
    lines = txt.split("\n")
    print()
    print("CMD:",cmd)
    print("============ CHECK OUTPUT ============")
    _exit = 99
    lines = txt.split("\n")
    if len(lines) <= 0:
        _exit = 2
        print("error no data from:", cmd)
        sys.exit(_exit)

    for line in lines:
        if "exit:" in line:
            try:
                x=line.split(":")[-1]
                x = x.strip()
                _exit = int(x)
                #print("set exit to:",_exit)
            except:pass


        print("",line)

    #'CPU'=value[UOM];[warn];[crit];[min];[max]
    #print("'CPU'=75;70;80;0;100")

finally:
    pass
sys.exit(_exit)
