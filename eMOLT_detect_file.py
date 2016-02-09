#!/usr/bin/env /anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:38:57 2015

@author: hxu
"""
import sys
import time
import logging
import win32gui,win32con,win32console
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
  
print "Please do not close real-time telemetry window."

# automactic minimize window
Minimize = win32gui.GetForegroundWindow()
time.sleep(1)
win32gui.ShowWindow(Minimize,win32con.SW_MINIMIZE)
# disable close buttom of python window
hwnd = win32console.GetConsoleWindow()
if hwnd:
   hMenu = win32gui.GetSystemMenu(hwnd, 0)
   if hMenu:
       win32gui.DeleteMenu(hMenu, win32con.SC_CLOSE, win32con.MF_BYCOMMAND)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(500)
            
    except KeyboardInterrupt:
        
        observer.stop()    
    observer.join()   

