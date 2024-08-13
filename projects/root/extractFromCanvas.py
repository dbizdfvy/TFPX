'''
Given a pixelalive test, gets the location and values of pixels where the return value isn't 1 
'''

import os
import ROOT

current_directory = os.path.dirname(os.path.realpath(__file__))
root_file = ROOT.TFile.Open(f"{current_directory}/../data/Module_data/RH0009/Run000000_PixelAlive.root")

hist = root_file["Detector"]["Board_0"]["OpticalGroup_0"]["Hybrid_0"]["Chip_12"]["D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)"].GetPrimitive("D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)")

rawData = []
badPixels = []
badValues = []

for bx in range(1,hist.GetNbinsX()):

    rawData.append([])


    for by in range(1,hist.GetNbinsY()+1):

        rawData[bx-1].append(hist.GetBinContent(bx,by))

        if hist.GetBinContent(bx,by) != 1.0: 
            badPixels.append([bx,by])
            badValues.append(hist.GetBinContent(bx,by))

#print(badPixels)
#print(badValues)
