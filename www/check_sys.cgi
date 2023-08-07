#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-2.0-only
# - flo932@uxsrv.de micha.r
import cgitb
cgitb.enable()

import os
#print(os.environ)
import sys

#print(sys.argv)
def get_args():
    print()
    data = {}
    if "QUERY_STRING" in os.environ:
        get = os.environ["QUERY_STRING"][:]
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
        #print("-",k,v)
        #print(data)

    #print()
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
dbg=0
if "verbose" in args:
    dbg=1
if dbg:print("TOKTENS",t)
if dbg:print(args)
if dbg:print("-_- "*20)


if "mode" in args:
    if "disk" in args["mode"]:
        cmd="/usr/bin/python3 /opt/check/check_disk.py"
        print("---------------")
        print("cmd",cmd)
        r=os.popen(cmd)
        for line in r.readlines():
            line = line.strip()
            print(line)
    elif "uptime" in args["mode"]:
        cmd="/usr/bin/python3 /opt/check/check_uptime.py"
        print("---------------")
        print("cmd",cmd)
        r=os.popen(cmd)
        for line in r.readlines():
            line = line.strip()
            print(line)

    elif "mount" in args["mode"]:
        cmd="sudo /opt/check/check_mount.sh"
        if "code" in args:
            if args["code"] == "B":
                cmd="sudo /opt/check/check_mountB.sh"
        print("---------------")
        print("cmd",cmd)
        r=os.popen(cmd)
        for line in r.readlines():
            line = line.strip()
            print(line)
    else:
        print("mode unknown",args["mode"])
else:
    print("no mode selected")
