import sys, os, ROOT
from array import array
cd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{cd}/..")
from utils import txtReader, getTDAC, column

def histo(coords, *argv):

    xcoords = column(coords,0)
    ycoords = column(coords,1)

    hist = ROOT.TH2F("hist", "title",len(xcoords),min(xcoords),max(xcoords),len(ycoords),min(ycoords),max(ycoords))

    for x, y in zip(xcoords, ycoords):
        hist.Fill(x, y)
    
    canvas = ROOT.TCanvas("canvas","2D Histogram",800,600)

    hist.Draw("COL")
    #hist.Scale(1.0 / hist.Integral())
    canvas.Update()
    canvas.SaveAs(argv[0])
    canvas.Show()
    canvas.WaitPrimitive()


#initializes and gets the variables from cmd
coords = getTDAC(sys.argv[1],sys.argv[2])
histo(coords, "TDAC-Map.png")
