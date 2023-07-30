#!/usr/bin/env python3
# 2022 GPL v2 only
# - flo932@uxsrv.de micha.r
import os
import subprocess
import sys

os.system("id")
_exit = 3
r=100

import os
import time
from datetime import datetime

r = os.popen("uptime -s")
x = r.read().strip()
s = datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
print(s)
c = unixtime = time.mktime(s.timetuple()) #/3600
uptime = (time.time()-c)/3600/24
uptime = round(uptime,2)
print(uptime,"days")
#sys.exit()

perf = []
_max = 100 # tage
_warn = 98
_min  =  0
_krit = 99
uptimes = [uptime]

for u in uptimes:
    if u > _max:
        #print("max",u,_max)
        _exit = 2 # 2 krit
    elif u > _krit:
        #print("krit",u,_krit)
        _exit = 2 # 2 krit
    elif u > _warn:
        #print("warn",u,_warn)
        _exit = 1 # 1 warn
    elif u < 0.40:
        #print("warn",u,"< 0.1")
        _exit = 1 # 1 warn
    else:
        _exit = 0 # 0 OK

    pf = "{:0.02f};{:0.02f};{:0.02f};{:0.02f};{:0.02f}".format(u,_warn,_krit,_min,_max)
    pf = "{:0.02f};{:0.02f};{:0.02f}".format(u,_warn,_krit,_min,_max)
    perf.append(pf)

level = ["OK","WARN","KRIT","UNKNOWN"]
if len(level) > _exit:
    print("LEVEL:",level[_exit])

print()
print("exit:",_exit)

# 0 OK
# 1 warning
# 2 krit
# 3 unknown

if perf:
    for i,p in enumerate(perf):
        print("|uptime{}=".format(i)+p)
print()


