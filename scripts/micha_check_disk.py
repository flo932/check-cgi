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

print( sys.argv )

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-a", "--addr", dest="addr",
                  help="host ip")
parser.add_option("", "--host", dest="host",
                  help="host name")

parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

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
#f = open("/tmp/env.log","w")
#f.write(str(x))
#f.close()
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

    cmd="curl http://{}:/sys/check_disk.cgi?token={}".format(h,t)
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

    #print("exit:",_exit)
    #print()
    #print(" --> | ",end="")
    #print(perf)
    #sys.exit(_exit)
finally:
    pass
sys.exit(_exit)
