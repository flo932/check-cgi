#!/usr/bin/env python3

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
from xtoken import token 
t = token()


if "token" not in args:
    print("not token")
    exit()

if args["token"] not in t:
    print("wrong token")
    exit()


cmd="ps aux | grep mysql"
cmd="ps -Ao %cpu,command  | grep /usr/sbin/mysqld"
cmd="ps -Ao %cpu,command  | sort -r | head"
cmd="top -bn1 | head" #-c
#cmd="mpstat -P 0,1"
#os.system(cmd)
x=os.popen(cmd)
print(x.read())
print("hu")





