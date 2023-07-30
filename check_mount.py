#!/usr/bin/env python3
import os

os.system("id")
exit = 0
#r = os.popen("df -hT")
#print(r.read())
fname="/mnt/server/m.rathfelder/infopool/PPS/PPS MA-BI-2012.mdb"
#print(fname)
r=os.path.isfile(fname)
#print(x.read())
print("is mounted infop/mdb:",r)
if not r:
    exit += 1

fname="/mnt/server/produktion/cimconcept/NCdaten/cnc.idx"
r=os.path.isfile(fname)
print("is mounted cim/nc/idx:",r)

if not r:
    exit += 1
#exit =1
print("exit:",exit)
metric=0
if metric:
    print("Metric:")
    print(" --> |",end="" ) 
    print(" 'CPU0'=75;70;80;0;100" ,end="")
    print(" 'CPU1'=60;70;80;0;100" ,end="")
    print()

