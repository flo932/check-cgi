#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-2.0-only
# - flo932@uxsrv.de micha.r

import os
#print(os.environ)
import sys
import _thread
import time

def kill_after(sec=30):
    import sys,os
    print("starting... timeout",sec,"sec")
    time.sleep(sec)
    print("time is over !!",__file__)
    os._exit(100) # hard exit
_thread.start_new_thread(kill_after,())


#print(sys.argv)
def get_args():
    data = {}
    if "QUERY_STRING" in os.environ:
        get = os.environ["QUERY_STRING"]
        if "&" in get:
            get = get.split("&") 
        else:
            get = [get]
        for a in get:
            if "=" in a:
                a = a.split("=",1)
                k = a[0]
                v = a[1]
                data[k] = v
        #print(data)

    return data

args = get_args()
    

sys.path.append("/opt/check/lib/")
from xtoken import token 
t = token()



if "token" not in args:
    print("not token")
    exit()

if args["token"] not in t:
    print("wrong token")
    exit()

import os

cmd="sudo /opt/check/check_mount.sh"
if "code" in args:
    if "B" == args["code"]:
        cmd="sudo /opt/check/check_mountB.sh"

print("---------------")
print("cmd",cmd)
r=os.popen(cmd)
for line in r.readlines():
    line = line.strip()
    print(line)
#time.sleep(31)
