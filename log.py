#!/usr/bin/env python
import sys
from AppKit import NSWorkspace
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)
import datetime
import os
import pyautogui as pag

def getActiveWindowTitle():
    global activeWindowTitle
    curr_app = NSWorkspace.sharedWorkspace().frontmostApplication()
    curr_pid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']
    curr_app_name = curr_app.localizedName()
    options = kCGWindowListOptionOnScreenOnly
    windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    txt = ""
    for window in windowList:
        pid = window['kCGWindowOwnerPID']
        windowNumber = window['kCGWindowNumber']
        ownerName = window['kCGWindowOwnerName']
        geometry = window['kCGWindowBounds']
        windowTitle = window.get('kCGWindowName', u'Unknown')
        if curr_pid == pid:
            activeWindowTitle = ownerName + " - " + windowTitle
    return activeWindowTitle

def main():
    bufWindowTitle = ""
    try:
        while True:
            dt_now = datetime.datetime.now()
            global activeWindowTitle
            activeWindowTitle = getActiveWindowTitle()
            if bufWindowTitle != activeWindowTitle:
                if "youtube" in activeWindowTitle or "YouTube" in activeWindowTitle or "Twitter" in activeWindowTitle or "Discord" in activeWindowTitle:
                    pag.keyDown("command")
                    pag.press("w")
                    pag.keyUp("command")
                print(activeWindowTitle,dt_now.strftime('%H:%M:%S') + "  " + str(dt_now.date()))
                bufWindowTitle = activeWindowTitle
                if os.path.exists("log/log"+str(dt_now.date())+".txt") == "False":
                    file = "log/log"+str(dt_now.date())+".txt"
                    fileobj = open(file, "x", encoding = "utf_8")
                    fileobj.write(activeWindowTitle + "  " + dt_now.strftime('%H:%M:%S') + "  " + str(dt_now.date()) + "\n")
                    fileobj.close()
                else:
                    file = "log/log"+str(dt_now.date())+".txt"
                    fileobj = open(file, "a", encoding = "utf_8")
                    fileobj.write(activeWindowTitle + "  " + dt_now.strftime('%H:%M:%S') + "\n")
                    fileobj.close()
    except KeyboardInterrupt:
        sys.exit(0)
if __name__ == '__main__':
    main()