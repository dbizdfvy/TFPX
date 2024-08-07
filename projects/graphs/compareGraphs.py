'''
Given paths to two RTD readout file, 
Trims the data to the given intervals according to splitFile function and overlays two of the graphs
'''

import ROOT, csv, os,sys
from array import array
sys.path.insert(1,'/home/yehyun/TFPX/final-codes/utils')
from pyutils import column, floatList, splitData, offSet, scale

def multiGraph(data):
    mg = ROOT.TMultiGraph()

    for i in range(len(data)):
        #gets the x and y coordinates for this set of data points
        x = data[i][0]
        y = data[i][1]


        graph = ROOT.TGraph(len(x),array('d',x),array('d',y))
        mg.Add(graph)

    
    canvas = ROOT.TCanvas("canvas","Multigraph Canvas",800,600)
    #mg.SetTitle("Comparison of Two Data Points")
    mg.Draw("A")

    canvas.Update()
    canvas.SaveAs("multigraph_variable.png")
    canvas.Show()

#paths to the RTD readout files.
pathA = r"/home/yehyun/data/port_card_0702.csv"
pathB = r"/home/yehyun/data/Port_card_0710.csv"

intervalsA = [[1006,1250],[1427,1537]]
intervalsB = [[2130,2192],[3728,3902]]

data = []

with open(pathA) as file:
    dataA = list(csv.reader(file))
   
    timeA = splitData(column(dataA,2),intervalsA)

    for i in range(len(timeA)):
        timeA[i] = floatList(timeA[i])
        timeA[i] = offSet(timeA[i],-1*timeA[i][0])
        timeA[i] = scale(timeA[i],1/(60*1000))

    tempA = splitData(column(dataA,13),intervalsA)

    for i in range(len(tempA)):
        tempA[i] = floatList(tempA[i])


data.append([])
data[0].append(timeA[0])
data[0].append(tempA[0])


with open(pathB) as file: 
    dataB = list(csv.reader(file))
    
    timeB = splitData(column(dataB,2),intervalsB)

    for i in range(len(timeB)):
        timeB[i] = floatList(timeB[i])
        timeB[i] = offSet(timeB[i],-1*timeB[i][0])
        timeB[i] = scale(timeB[i],1/(60*1000))

    tempB = splitData(column(dataB,13),intervalsB)

    for i in range(len(tempB)):
        tempB[i] = floatList(tempB[i])


data.append([])
data[1].append(timeB[0])
data[1].append(tempB[0])

multiGraph(data)
