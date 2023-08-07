#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-2.0-only
# - flo932@uxsrv.de micha.r
import os
import subprocess


cmd='/usr/bin/checkzfs --remote={pve} --filter tank/{ds} --replicafilter etank/crypt-repl/{ds}  --prefix ""'
cmd=cmd.format(ds="everest" ,pve="router01")
#cmd="ls -l"
print(cmd)

r = os.popen(cmd)
if not r:
    _exit += 1
lines = r.readlines()
print("---")

import json
perf = []
_max = 79
_exit = 3 #unknown

if lines:
    for line in lines:
        line=line.strip()
        j=line
        print("line:",line)
        continue 


        try:
            u = 10 #int(j["CAP"][:-1])

            if u > _max:
                _exit = 2 # krit
            if u > _max-5:
                if _exit not in [2]: #== 3:
                    _exit = 1 # warn


            pf = "|{}={};{};{}".format(d,u,_max-10,_max)
            perf.append(pf)
        except Exception as e:print(e)
print()
print("exit:",_exit)

if perf:
    for i,p in enumerate(perf):
        print(p)
print()

