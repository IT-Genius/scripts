#!/usr/bin/python
#----------------------------------------
#
# Create file named by date of today
# by Gennadiy
#
#-----------------------------------------

import datetime

dateToday = datetime.date.today()					#date and time now
fileName = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")	#pattern
fileDir = '/var/tmp/'+fileName						#dir to save file
#print("Date today: " + str(dateToday))
#print(fileDir)

myfile = open(fileDir, mode='w')					#creation file
#myfile.write()
myfile.close()

