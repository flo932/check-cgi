#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-2.0-only
# - flo932@uxsrv.de micha.r
import os
import subprocess

os.system("id")
_exit = 3
r=100
cmd="free -m| tail -n 2 | xargs  | jq -R 'split(\" \")|{all:.[1],used:.[2],free:.[6]}'"
print(cmd.replace("|","I"))
#r = subprocess.Popen([cmd])a
r = os.popen(cmd)
#print(dir(r))
#if not r:
#    _exit += 1
#exitcode = writer.wait()
txt = r.read()
#print(txt)
import json
j = json.loads(txt)
print(j)
perf = []
_max = 95
_warn = 90
_min = 0
if "free" in j and "all" in j:
    pf = "|mem="
    try:
        f = int(j["free"])
        a = int(j["all"])
        u = a-f #f/a # used in %
        _warn = int(a*0.90)
        _krit = int(a*0.95)
        _max  = a 
        #u = a/f-1 # used in %
        #u = f/(a/100)
        #u = (f)/(a/100)
        print("used: {:0.02f} k".format(u) )

        if u > _krit:
            _exit = 2 # 2 krit
        elif u > _warn:
            _exit = 1 # 1 warn
        else:
            _exit = 0 # 0 OK
        pf = "{:0.02f};{:0.02f};{:0.02f};{:0.02f};{:0.02f}".format(u,_warn,_krit,_min,_max)

        perf.append(pf)
    except Exception as e:
        print(e)
        _exit = 3
print()
print("exit:",_exit)

# 0 OK
# 1 warning
# 2 krit
#

if perf:
    for i,p in enumerate(perf):
        print("|mem{}=".format(i)+p)
print()



