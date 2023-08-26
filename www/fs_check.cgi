#!/usr/bin/env python3
print( "Content-Type: text/html")
print()

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
    
import hashlib
import time

def token():
    secret="Eeth0eekoov4"
    t = str(int(time.time()/100))+"_"+secret
    #print(t)
    try:
        b=bytes(t,"ascii")
    except:
        b=bytes(t) #,"ascii")
    hash_object = hashlib.sha224(b)
    hex_dig = hash_object.hexdigest()
    #print(hex_dig)
    t=hex_dig #+"-"
    return t

t = token()



if 0:
    if "token" not in args:
        print("not token")
        exit()

    if t != args["token"]:
        print("wrong token")
        exit()

print("<pre>")
import subprocess as sp
_exit=10 # init 
def CMD(cmd):
    global _exit
    print("<br>")
    print("CMD:",cmd)
    print("<br>")
    pipe = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE )
    #print(str([x.read()]).replace("<","&lt;"))
    #print(str([x,x.read()]).replace("<","&lt;"))
    # res = tuple (stdout, stderr)
    res = pipe.communicate()
    print("retcode =", pipe.returncode)
    print("stdout =", res[0])
    print("stderr =", res[1])
    if res[1]:
        #print("exit 10")
        _exit = 5
    else:
        print("exit 0")
        if _exit == 10:
            _exit = 0
    #print("<br>")

tmp = "/tmp/schreibtest.txt"

cmd="echo $(date) > {}".format(tmp)
CMD(cmd)

cmd="cat {}".format(tmp)
CMD(cmd)


#for i in dir(x):
#    print(i,"<br>")


print("<br>")
print("<br>")
print()
print("exit:",_exit)
print()
exit(_exit)
