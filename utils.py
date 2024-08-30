import os, numpy, ROOT
from array import array

def column(matrix,i):
    return [row[i] for row in matrix]

def txtReader(filePath, i):
    with open(filePath) as file:
        
        #final matrix. 1st index is the row, 2nd index is the column in the txt file.

        txtMatrix = []

        #matches each parameter to an index

        index = ['ENABLE','HITBUS','INJEN','TDAC']

        for line in file:

            linelist = line.split()
            
            if len(linelist) > 0:
                if linelist[0] == index[i]:
                    txtMatrix.append([float(n) for n in linelist[1].split(",")])


    return txtMatrix

def getNoisy(txtData):
    
    coords = []

    for i in range(len(txtData)):
        for j in range(len(txtData[i])):
            if txtData[i][j] != 1.0:

                coords.append([i,j])

    return coords

def getNewNoisy(oldFilePath, newFilePath):
    
    oldData = getNoisy(txtReader(oldFilePath,0))
    newData = getNoisy(txtReader(newFilePath,0))

    newSet = set(map(tuple,newData))
    diff = [coord for coord in oldData if tuple(coord) not in newSet]

    return diff

def getTDAC(filePath, TDAC, *args):

    rootFile = ROOT.TFile.Open(filePath)
    dist = rootFile["Detector"]["Board_0"]["OpticalGroup_0"]["Hybrid_0"]["Chip_12"]["D_B(0)_O(0)_H(0)_TDAC2D_Chip(12)"].GetPrimitive("D_B(0)_O(0)_H(0)_TDAC2D_Chip(12)")

    coords = [[],[]]

    for bx in range(1,dist.GetNbinsX()+1):
        for by in range(1,dist.GetNbinsY()+1):

            bz = dist.GetBinContent(bx,by)

            if bz >= float(TDAC):
                coords[1].append([bx,by])
            else:
                coords[0].append([bx,by])

    if len(args) == 0:
        return coords[1]
    else:
        return coords

'''
def getDead(filePath):
    
    rootFile = ROOT.TFile.Open(filePath)
    hist = rootFile["Detector"]["Board_0"]["OpticalGroup_0"]["Hybrid_0"]["Chip_12"]["D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)"].GetPrimitive("D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)")

    #final data. Stored are the pixel coordinates
    data = []

    for bx in range(1,hist.GetNbinsX()+1):
        for by in range(1,hist.GetNbinsY()+1):
            if hist.GetBinContent(bx,by) != 1.0:
                data.append([bx,by])

    return data

def getNewDead(oldFilePath, newFilePath):

    oldData = getDead(oldFilePath)
    newData = getDead(newFilePath)

    oldSet = set(map(tuple,oldData))
    diff = [coord for coord in newData if tuple(coord) not in oldSet]

    return diff
'''    

#caution! Requires *argv to be [[x1],[y1]], [[x2],[y2]], [[x3],[y3]], ... 
def multiGraph(*argv):
    mg = ROOT.TMultiGraph()

    for arg in argv:
        #gets the x and y coords for ith set of points
        x = arg[0]
        y = arg[1]

        graph = ROOT.TGraph(len(x),array('d',x),array('d',y))
        mg.Add(graph)

    canvas = ROOT.TCanvas("canvas","Multigraph Canvas",800,600)
    mg.Draw("A")
    
    canvas.Update()
    #canvas.SaveAs("multigraph.png")
    canvas.Show()

#same requirements as multigraph
def multiHist(*argv):
    mh = ROOT.THStack()

    argMin = 0
    argMax = 0

    for arg in argv:
        if min(arg) < argMin:
            argMin = min(arg)
        if max(arg) > argMax:
            argMax = max(arg)


    for arg in argv:
        hist = ROOT.TH1F("name","title",len(arg),argMin,argMax)
        
        for point in arg:
            hist.Fill(point)

        mh.Add(hist)

    canvas = ROOT.TCanvas("canvas","Multihist Canvas",800,600)
    mh.Draw()

    canvas.Update()
    #canvas.SaveAs("Multihist.png")
    canvas.Show()
    canvas.WaitPrimitive()

#same requirements as multigraph
def getNoise(filePath, *argv):
    
    rootFile = ROOT.TFile.Open(filePath)
    hist = rootFile["Detector"]["Board_0"]["OpticalGroup_0"]["Hybrid_0"]["Chip_12"]["D_B(0)_O(0)_H(0)_Noise2D_Chip(12)"].GetPrimitive("D_B(0)_O(0)_H(0)_Noise2D_Chip(12)")

    noise = []

    for arg in argv:

        noise.append([])

        x = arg[0]
        y = arg[1]

        for i in range(min(len(x),len(y))):

            #don't forget the root starts from 1
            noise[-1].append(hist.GetBinContent(x[i]+1,y[i]+1))

    return noise

def getThreshold(filePath, *argv):

    rootFile = ROOT.TFile.Open(filePath)
    hist = rootFile["Detector"]["Board_0"]["OpticalGroup_0"]["Hybrid_0"]["Chip_12"]["D_B(0)_O(0)_H(0)_Threshold2D_Chip(12)"].GetPrimitive("D_B(0)_O(0)_H(0)_Threshold2D_Chip(12)")

    threshold = []

    for arg in argv:

        threshold.append([])

        x = arg[0]
        y = arg[1]

        for i in range(min(len(x),len(x),len(y))):

            threshold[-1].append(hist.GetBinContent(x[i]+1,y[i]+1))

    return threshold

def getSCurve(filePath, x, y):

    rootFile = ROOT.TFile.Open(filePath)
    scurve = rootFile["Detector"]["Board_0"]["OpticalGroup_0"]["Hybrid_0"]["Chip_12"]["D_B(0)_O(0)_H(0)_SCurveMap_Chip(12)"].GetPrimitive("D_B(0)_O(0)_H(0)_SCurveMap_Chip(12)")

    vcal = []
    efficiency = []

    for bz in range(1,scurve.GetNbinsZ()+1):
        vcal.append(bz)
        efficiency.append(scurve.GetBinContent(x,y,bz))

    return [vcal,efficiency]
