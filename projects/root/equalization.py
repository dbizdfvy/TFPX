'''
Equalization map. Given a 3d histogram with the fourth variable being the equalization value, 
Graphs the points with abnormal (>31 equalization) values.
'''

import os
import ROOT
from noiseScanCheck import TwoDhist

current_directory = os.path.dirname(os.path.realpath(__file__))
distFile = ROOT.TFile.Open(f"{current_directory}/../data/Module_data/RH0017/Run000026_ThrEqualization.root")
dist = distFile["Detector"]["Board_0"]["OpticalGroup_0"]["Hybrid_0"]["Chip_12"]["D_B(0)_O(0)_H(0)_TDAC2D_Chip(12)"].GetPrimitive("D_B(0)_O(0)_H(0)_TDAC2D_Chip(12)")

xcoords = []
ycoords = []
zcoords = []

for bx in range(1,dist.GetNbinsX()+1):
    for by in range(1,dist.GetNbinsY()+1):

        bz = dist.GetBinContent(bx,by)

        if bz >= 31:
            xcoords.append(bx)
            ycoords.append(by)
            zcoords.append(bz)

TwoDhist(xcoords,ycoords,zcoords)
