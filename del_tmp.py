#!/usr/bin/python
# ----------------------------------------
#
# Delete files older then 15 min
# by Gennadiy
#
# -----------------------------------------

import os
import time

folder = "/var/tmp"
nowTime = time.time()        # get current time in sec
ageTime = nowTime - 60 * 15  # current time - 60 sec * 15 = 15 min ago (in seconds)


def delete_old_files(folder):
    for file in os.listdir(folder):
        #print(file)
        fileDir = os.path.join(folder, file)            #fool way to file
        fileTime = os.path.getmtime(fileDir)            #time in second from last modification / creation
        #print(str(fileTime))
        if fileTime < ageTime:                          #if files older then 15 min
            #print("bye bye: " + str(file))
            os.remove(fileDir)                          #delete files

# -----main------
delete_old_files(folder)
