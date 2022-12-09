#!/usr/bin/env python

import sys

# Mac用

from AppKit import NSWorkspace
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)
import datetime

def getActiveWindowTitle():
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
                print(activeWindowTitle,dt_now.strftime('%H:%M:%S'))
                bufWindowTitle = activeWindowTitle
    except KeyboardInterrupt:
        sys.exit(0)
if __name__ == '__main__':
    main()