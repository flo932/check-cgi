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
import xtoken 
t = xtoken.token()

xtoken.check(args,t)




cmd="sudo /opt/check/check_disk.sh"
cmd="/usr/bin/python3 /opt/check/check_disk.py"
print("---------------")
print("cmd",cmd)
r=os.popen(cmd)
for line in r.readlines():
    line = line.strip()
    print(line)
