import sys, os, ROOT
cd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{cd}/..")
from utils import getNewNoisy, getNoise, getThreshold, multiHist, column

#initializes and gets the variables from cmd
oldTxt = sys.argv[1]
newTxt = sys.argv[2]
oldSC = sys.argv[3]
newSC = sys.argv[4]

#gets and graphs the data
coords = getNewNoisy(newTxt, oldTxt)
cols = [column(coords,0),column(coords,1)]

oldNoise = getNoise(oldSC,cols)
newNoise = getNoise(newSC,cols)
oldThreshold = getThreshold(oldSC,cols)
newThreshold = getThreshold(newSC,cols)

multiHist(oldNoise[0],newNoise[0])
multiHist(oldThreshold[0],newThreshold[0])
