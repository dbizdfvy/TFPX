'''
Given:
    a folder with IR images with timestamps as their filename,
    a path to a vertices file, 
    a path to an RTD readout log,
    and a path to a csv file for logging data,
For each IR image file in the folder, 
averages the temperatures in the selected areas specified by the vertices file,
and does a linear approximation to get the RTD temperature at the time the IR image was taken.

The averaged IR temperature and the RTD temperature are logged for calibration
'''

import os, csv, sys, pandas as pd
sys.path.insert(1,'/home/yehyun/TFPX/final-codes/utils') #need to rewrite this
from excelCoords import excelCoords
from polygon import polyPoints
from pyutils import closest, linApprox

def polyAverage(vPath, fPath):
    coords = excelCoords(vPath)
    with open(fPath) as file:
        data = list(csv.reader(file))

    num = 0

    for i in range(len(coords)):
         num += float(data[coords[i][0]][coords[i][1]])

    return num/len(coords)

#Gets the file paths. Replacing the input statements with static variables is recommended.
dirPath = input("Input IR folder filepath: ")
vPath = input("Input vertices filepath: ")
rPath = input("Input RTD filepath: ")
wPath = input("Input write filepath: ")


RTDtimes = []
RTDtemps = []

#get data from the RTD csv
with open(rPath) as file:
    #initializes and skips the header row
    reader = csv.reader(file)
    next(file)

    for row in reader:
        #assumes that 2nd row are the times in the format
        #hous.minute.second.millisecond
        #assumes that the 9th row are the RTD temperatures
        RTDtimes.append(float(row[1][:2])*3600+float(row[1][3:5])*60+float(row[1][6:]))
        RTDtemps.append(float(row[10]))

#gets list of files in the directory
files = os.listdir(dirPath)
fields = ["RTD temperature", "IR temperature"]

#initializes and writes the headers
with open(wPath, 'w', newline = '') as writefile: 
    writefile.truncate()
    writer = csv.writer(writefile)
    writer.writerow(fields)

    #loops over all files in the directory
    for file in files:
        #gets the full path of a looped file
        fPath = os.path.join(dirPath, file)
        #gets the time and temperature from the IR image file
        IRtime = float(file[9:11])*3600+float(file[12:14])*60+float(file[15:17])
        IRtemp = polyAverage(vPath, fPath)
        #gets the RTD time closest to the IR time and linearly approximates the RTD temperature
        #passes on edge cases
        closestTime = closest(RTDtimes, IRtime)

        try: 
            approxTemp = linApprox(RTDtimes[closestTime],RTDtemps[closestTime],RTDtimes[closestTime+1],RTDtemps[closestTime+1],IRtime)
            writer.writerow([approxTemp,IRtemp])
        except IndexError:
            pass
