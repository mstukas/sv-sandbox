#!/usr/bin/python3

import sys,os,time,re
if __name__ == '__main__':
    print ("scrap paper\n")

    swversion = []
    version = os.popen("uname -a")
    cdir = os.popen("pwd")

    for line in version:
        swversion.append(line)
     


    for line in cdir:
        swversion.append(line)



    version.close()
    cdir.close()

    L = [print (line) for line in swversion]

    #edit file from master branch
    #edit from Git Bash

