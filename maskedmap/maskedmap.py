import sys, os, ROOT
from array import array
cd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{cd}/..")
from utils import txtReader, getNoisy, getNewNoisy, column

def histo(coords, *argv):

    xcoords = column(coords,0)
    ycoords = column(coords,1)

    hist = ROOT.TH2F("hist", "title",len(xcoords),min(xcoords),max(xcoords),len(ycoords),min(ycoords),max(ycoords))

    for x, y in zip(xcoords, ycoords):
        hist.Fill(x, y)
    
    canvas = ROOT.TCanvas("canvas","2D Histogram",800,600)

    hist.Draw("COLZ")
    #hist.Scale(1.0 / hist.Integral())
    canvas.Update()
    canvas.SaveAs(argv[0])
    canvas.Show()
    canvas.WaitPrimitive()


#initializes and gets the variables from cmd
oldTxt = txtReader(sys.argv[1],1)
newTxt = txtReader(sys.argv[2],1)

oldCoords = getNoisy(oldTxt)
newCoords = getNoisy(newTxt)
diffCoords = getNewNoisy(sys.argv[2], sys.argv[1])

histo(oldCoords, "Old-Map.png")
histo(newCoords, "New-Map.png")
histo(diffCoords, "Difference-Map.png")
