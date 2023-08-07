#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-2.0-only
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
      "-c" = "$cmd$"
      "-t" = "$token$"
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

import xxx_token as token

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
_exit = 3 #100
try:
    h="192.168.0.28"
    if "-a" in sys.argv:
        i = sys.argv.index("-a")
        _h=sys.argv[i+1]
        h = _h
    while ".." in h:
        h = h.replace("..","")
    while "/" in h:
        h = h.replace("/","")

    c = "check_mem.cgi"
    if "-c" in sys.argv:
        i = sys.argv.index("-c")
        _h=sys.argv[i+1]
        c = _h
    while ".." in c:
        c = c.replace("..","")
    while "/" in c:
        c = c.replace("/","")

    m = "check_mem.cgi"
    if "-m" in sys.argv:
        i = sys.argv.index("-m")
        _h=sys.argv[i+1]
        m = _h
    while ".." in m:
        m = m.replace("..","")
    while "/" in m:
        m = m.replace("/","")

    code = ""
    if "-code" in sys.argv:
        i = sys.argv.index("-code")
        _h=sys.argv[i+1]
        code = _h
    while ".." in code:
        code = code.replace("..","")
    while "/" in m:
        code = code.replace("/","")
    cmd="curl -L -k 'http://{}:/sys/{}?token={}&mode={}&code={}'".format(h,c,t,m,code)
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
            except Exception as e:print("_exit",e)

    print("exit:",_exit)
    print()
    #print(" --> | ",end="")
    #print(perf)

finally:
    sys.exit(_exit)
