import sys, os, ROOT, numpy as np
from array import array
cd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{cd}/..")
from utils import getSCurve

#initializes and gets the variables from cmd
filePath = sys.argv[1]
xcoord = int(sys.argv[2]) + 1
ycoord = int(sys.argv[3]) + 1

data = getSCurve(filePath, xcoord, ycoord)
xlist = data[0]
ylist = data[1]

#graphs the data
gm = ROOT.TGraph(len(xlist),array('d',xlist),array('d',ylist))
gm.SetMarkerStyle(20)
gm.SetMarkerSize(1.5)

gl = ROOT.TGraph(len(xlist),array('d',xlist),array('d',ylist))
gl.SetLineColor(ROOT.kBlue)
gl.SetLineWidth(2)

canvas = ROOT.TCanvas("canvas","Lined Graph",800,600)

gm.Draw("AP")
gl.Draw("L")

gm.SetTitle("SCurve at "+"("+str(xcoord)+","+str(ycoord)+")")
gm.GetXaxis().SetTitle("VCal")
gm.GetYaxis().SetTitle("Efficiency")

canvas.Update()
canvas.Draw()
#canvas.SaveAs("SCurve-Disabled.png")
canvas.WaitPrimitive()
