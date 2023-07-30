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



x=os.environ
x=dict(x)
x= sys.argv
#f = open("/tmp/env.log","w")
#f.write(str(x))
#f.close()
print( sys.argv )
_exit = 100
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

    cmd="curl http://{}:/sys/index.cgi?token={}".format(h,t)
    cmd += " 2> /dev/null"
    x=os.popen(cmd)
    #print(x)
    txt=x.read()
    lines = txt.split("\n")
    i=0
    c=0
    error=0
    out=OrderedDict()
    ok=1
    for line in lines:
        if line == "EOB:":
            break
        line=line.strip()
        while "  " in line:
            line=line.replace("  "," ")

        line=line.split(" ")
        if len(line) == 12:
            cpu = 0
            print(i,len(line),[line])
            print(line[8])

            try:
                xcpu = line[8]
                xcpu = xcpu.replace(",",".")
                xcpu = float(xcpu)

                cpu = xcpu

                if cpu >= 70:
                    error += 1
                    print("CPU HIGH::",c,cpu,end="\t ")#,line[3][:20])
                else:
                    print("CPU OK::",c,cpu,end="\t ")#,line[3][:20])
                    ok+=1
            except ValueError as e:
                pass
            finally:pass
            if 1: #ok:
                k="cpu "+str(i)
                out[k] = cpu

        i+=1
    print()
    print()
    #print("argv",sys.argv)
    print(cmd)
    print(out)
    print(txt)
    def data(out):
        c=0
        _exit = 0
        txt=""
        for k in out:
            v=out[k]
            txt+="'CPU {}'={:0.0f};50;80;0;150 ".format(c,v)
            c+=1

        #'CPU'=value[UOM];[warn];[crit];[min];[max]
        #print(txt)
        return txt #_exit

    if error:# or not ok:
        print("ERROR")
        perf = data(out)
        _exit = 2
    else:
        print("OK")
        perf = data(out)
        _exit = 0
    print("exit:",_exit)
    print()
    print(" --> | ",end="")
    print(perf)
    sys.exit(_exit)
finally:
    pass
sys.exit(_exit)
