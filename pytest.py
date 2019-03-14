#!/usr/bin/python3
'''
scratch paper
'''
#import pexpect,subprocess 

import sys,os,time,re
if __name__ == '__main__':
    #print ("[breeze connector app]\n\n")

    # Option 1:
    t0 = time.clock()
    ifconfig = os.popen("netstat")
    interfaces = ifconfig.readlines()
    for i in interfaces:
        if "tmp" in i:
            print(i)
    ifconfig.close()
    t1 = time.clock()
    option1time = round(t1 - t0, 6)

    # Option 2:
    t2 = time.clock()
    ifconfig = os.popen("netstat")
    interfaces = ifconfig.readlines()
    int2 = [print(i) for i in interfaces if "tmp" in i]  # or "addr" in i]
    ifconfig.close()
    t3 = time.clock()
    option2time = round(t3 - t2, 6)

    print("Results: using time.clock()")
    print("Option #1 run time: ", option1time)
    print("Option #2 run time: ", option2time)

    if option1time < option2time:
        print("Option 1 is faster by: {0:.3f}% {1:.6f}sec".format(100-option1time/option2time*100,option2time-option1time))
    elif option2time < option1time:
        print("Option 2 is faster by: {0:.3f}% {1:.6f}sec".format(100-option2time/option1time*100,option1time-option2time))
    else:
        print("tie\n")
    ###############################################################################

    print ("\n")
    # Option 1:
    t0 = time.time()
    ifconfig = os.popen("netstat")
    interfaces = ifconfig.readlines()
    for i in interfaces:
        if "tmp" in i:
            print(i)
    ifconfig.close()
    t1 = time.time()
    option1time = round(t1 - t0, 6)

    # Option 2:
    t2 = time.time()
    ifconfig = os.popen("netstat")
    interfaces = ifconfig.readlines()
    int2 = [print(i) for i in interfaces if "tmp" in i]  # or "addr" in i]
    ifconfig.close()
    t3 = time.time()
    option2time = round(t3 - t2,6)

    print("Results: using time.time()")
    print("Option #1 run time: ", option1time)
    print("Option #2 run time: ", option2time)

    if option1time < option2time:
        print("Option 1 is faster by: {0:.3f}% {1:.6f}sec".format(100-option1time/option2time*100,option2time-option1time))
    elif option2time < option1time:
        print("Option 2 is faster by: {0:.3f}% {1:.6f}sec".format(100-option2time/option1time*100,option1time-option2time))
    else:
        print("tie\n")

    print ("\n\nProgram complete: ",time.asctime(time.localtime(time.time())))