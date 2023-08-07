#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-2.0-only
# - flo932@uxsrv.de micha.r

import hashlib
import time
import os
import sys

def token(secret="Eeth0eekoov4"):
    psk = ["/opt/check/psk","/etc/icinga2/scripts/xxx_psk"]
    flag = 0
    for p in psk:
        if os.path.isfile(p):
            f=open(p)
            tt = f.readlines()[0]
            secret = tt.strip()
            flag = 1
            break
    if flag == 0:
        print("WARNING NO psk FOUND !")
    t = str(int(time.time()/100))+"_"+secret
    #print(t)
    b=bytes(t,"ascii")
    hash_object = hashlib.sha224(b)
    hex_dig = hash_object.hexdigest()
    t=hex_dig #+"-"
    return t

