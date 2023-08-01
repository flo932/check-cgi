#!/usr/bin/python3

import os
import time
import sys

_exit=100 # default exit code

try:
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url",default="https://127.0.0.1/index.html",
                      help="set url" )
    parser.add_option("-p", "--pattern", dest="pattern",default="Login",
                      help="set search pattern" )
    parser.add_option("-P", "--Pattern", dest="Pattern",default="",
                      help="set search pattern" )
    parser.add_option("-s", "--stamp-format", dest="stamp",default="",
                      help="set search date %Y-%m-%d" )
    parser.add_option("-d", "--time-delta", dest="tdelta",default="",
                      help="timedelta in sec" )
    parser.add_option("-v", "--verbose", dest="verbose",default="",
                      help="show mor info's" )
    (options, args) = parser.parse_args()

    print(sys.argv)
    print("sys.argv")

    cmd="curl '{url}' 2>/dev/null ".format(url=options.url)

    pattern = []
    pattern2 = []

    if options.pattern:
        pattern.append( options.pattern) 

    if options.Pattern:
        pattern2.append( options.Pattern) 

    tdelta=0
    if options.tdelta:
        tdelta = options.tdelta

    if options.stamp:
        try:
            t = int(tdelta)
            t = time.localtime(time.time()-t)
            pattern.append(time.strftime(options.stamp,t))
        except Exception as e:
            print("exc",e)

    print()
    print("<br>")
    print("cmd",cmd)
    print("<br>")
    r=os.popen(cmd)
    lines = r.readlines()
    print("len lines",len(lines))
    print("<br>")
    print("pattern:",pattern)
    print("<br>")
    for i,line in enumerate(lines[1:]):
        ok = 0
        line = line.strip()
        if options.verbose:
            print(">>",line)
            print("<br>")
        

        for p in pattern:
            if p in line:
                #print(i,p,">",line.replace("<",""))
                ok += 1
                if options.verbose:
                    print("OK1",[ok,p,len(pattern)])
                    print("<br>")


        if ok >= len(pattern) and len(pattern) > 0:
            print("B1",[i,p,">",line.replace("<","")])
            print("<br>")
            _exit = 0
            break


        # -----------------------------------

        ok2 = 0
        for p in pattern2:
            if p in line:
                #print(i,p,">",line.replace("<",""))
                ok2 += 1
                if options.verbose:
                    print("OK2",[ok2,p,len(pattern2)])
                    print("<br>")


        if ok2 >= len(pattern2) and len(pattern2) > 0:
            print("B2",[i,p,">",line.replace("<","")])
            print("<br>")
            _exit = 0
            break
finally:
    print("<br>")
    print("exit:",_exit)
    print("<br>")
    print()
    print("|exit={exit};3;10;1".format(exit=_exit))
    exit(_exit)

