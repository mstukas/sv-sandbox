#!/usr/bin/env python
"""
Sandbox for Tkinter
"""
import time,sys,os
from Tkinter import *   

if __name__ == '__main__':
    print ("test Tk")
    
   
    class App:

        def __init__(self, master):

            frame = Frame(master)
            frame.pack()
            mainframe = Frame(root, height = 200, width = 500)
            mainframe.pack_propagate(0)
            mainframe.pack(padx = 5, pady = 5)
            self.button = Button(
                                 frame, text="QUIT", fg="red", command=frame.quit
                                 )
            self.button.pack(side=LEFT)

            self.hi_there = Button(frame, text="Hello", command=self.say_hi)
            self.hi_there.pack(side=LEFT)

        def say_hi(self):
            print "hi there, everyone!"

    root = Tk()

    app = App(root)

    root.mainloop()