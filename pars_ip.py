#!/usr/bin/python
#----------------------------------------
#
# Create file named by date of today
# by Gennadiy
# Looking for unique IP in log file
#
#-----------------------------------------

import re

input_file_way = "syslog"                               #way to log file
output_file_way = "unique_IPlist.txt"                   #output file

input_file = open(input_file_way, mode='r')             #open input file (our log)
resultIPfile = open(output_file_way, mode='w')          #create result file
mytext = input_file.read()                              #read log file

lookfor = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"     #pattern for IP

results = re.findall(lookfor, mytext)                   #find all IP in log
uniqueIP = ['0']
uniqueIP[0] = results[0]
print("len(results) : " + str(len(results)))            #How much IP we have

for item in results:                                    #Loop
    if item not in uniqueIP:                            #looking for duplicate
        uniqueIP.append(item)                           #append IP to new list

print("unique ip : " + str(len(uniqueIP)))

for item in uniqueIP:                                   #write file
    resultIPfile.write(item + "\n")

input_file.close()                                      #close openned file
resultIPfile.close()                                    #close openned file