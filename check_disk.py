#!/usr/bin/env python3
# 2022 GPL v2 only
# - flo932@uxsrv.de micha.r

import os
import subprocess

os.system("id")
_exit = 0
r=100
cmd="free -m| tail -n 2 | xargs  | jq -R 'split(\" \")|{all:.[1],used:.[2],free:.[6]}'"
cmd="df -lmT | grep -v tmpfs "
cmd="""df -lmT | grep -v "tmpfs\|fuse" | tail -n +2 | sed 's/[ ][ ]*/ /g' |  jq -R 'split(" ")|{disk:.[0],fs:.[1],free:.[4],used:.[5],mount:.[6]}| join(", ")'"""
cmd="""df -lmT | grep -v "tmpfs\|fuse" | tail -n +2 | sed 's/[ ][ ]*/ /g' |  jq -R 'split(" ")|{disk:.[0],fs:.[1],free:.[4],used:.[5],mount:.[6]}'"""
print(cmd.replace("|","I"))
#r = subprocess.Popen([cmd])a
r = os.popen(cmd)
#print(dir(r))
if not r:
    _exit += 1
#exitcode = writer.wait()
txt = r.read()
txt = "["+txt.replace('}\n{','},\n{')+"]"
#print(txt)
import json
perf = []
_max = 80
_exit = 3 #unknown
if txt:
    jj = json.loads(txt)
    for j in jj:
        if "used" in j and "disk" in j:

            d = j["disk"]
            try:
                u = int(j["used"][:-1]) #f/a # used in %
                #print("used: {} %".format(u) )

                if u > _max:
                    _exit = 2 # krit
                if u > _max-10:
                    if _exit == 3:
                        _exit = 1 # warn
                else:
                    if _exit == 3:
                       _exit = 0
                pf = "|{}={};{};{}".format(d,u,_max-10,_max)
                #print(pf)
                perf.append(pf)
            except Exception as e:print(e)
print()
#_exit = 3 #unbek
print("exit:",_exit)


if perf:
    for i,p in enumerate(perf):
        #print("|disk{}=".format(i)+p)
        print(p)
print()

