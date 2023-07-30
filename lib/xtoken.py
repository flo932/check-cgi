#!/usr/bin/python3
import os
import sys
import hashlib
import time

def _token(secret="",delta=0):
    #print(time.time())
    psk="/opt/check/psk"
    if os.path.isfile(psk):
        f = open(psk)
        secret=f.readlines()[0]
        f.close()
        secret = secret.strip()
    else:
        print("NO TOKEN FOUND !")
    if not secret:
        return ["no secret !"]
    #print("s:",secret)
    t = str(int((time.time()+delta)/100))+"_"+secret
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

def token(secret=""):
    #print("s::",secret)
    t1 = _token(secret,-60)
    t2 = _token(secret)
    t3 = _token(secret,60)
    out = [t1,t2,t3]
    #print(out)
    return out

def check(args,t):
    if "token" not in args:
        print("not token")
        exit()

    if args["token"] not in t:
        print("wrong token")
        exit()

