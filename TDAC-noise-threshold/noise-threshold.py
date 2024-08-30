import sys, os, ROOT
cd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{cd}/..")
from utils import getTDAC, getNoise, getThreshold, multiHist, column

def normalizedHist(list1, list2, name):

    lowerBound = min(min(list1),min(list2))
    upperBound = max(max(list1),max(list2))

    hist1 = ROOT.TH1F("hist1",name,100,lowerBound,upperBound)
    hist2 = ROOT.TH1F("hist2",name,100,lowerBound,upperBound)

    for value in list1:
        hist1.Fill(value)

    for value in list2:
        hist2.Fill(value)

    hist1.Scale(1.0/hist1.Integral())
    hist2.Scale(1.0/hist2.Integral())

    canvas = ROOT.TCanvas("canvas","Canvas",800,600)

    hist1.SetLineColor(ROOT.kBlue)
    hist1.Draw("HIST")

    hist2.SetLineColor(ROOT.kRed)
    hist2.Draw("HIST SAME")

    legend = ROOT.TLegend(0.7,0.7,0.9,0.9)
    legend.AddEntry(hist1, "normal TDAC","l")
    legend.AddEntry(hist2, "high TDAC","l")
    legend.Draw()

    canvas.Update()
    canvas.SaveAs(str(name)+".png")
    canvas.Show()
    canvas.WaitPrimitive()

#initializes and gets the varibles from cmd
thrEqualization = sys.argv[1]
TDAC = sys.argv[2]
sCurve = sys.argv[3]

#gets and graphs the data
coords = getTDAC(thrEqualization, TDAC,1)
lowCols = [column(coords[0], 0), column(coords[0],1)]
highCols = [column(coords[1],0), column(coords[1],1)]

lowNoise = getNoise(sCurve,  lowCols)
lowThreshold = getThreshold(sCurve, lowCols)
highNoise = getNoise(sCurve, highCols)
highThreshold = getThreshold(sCurve, highCols)

normalizedHist(lowNoise[0],highNoise[0],"TDACnoise")
normalizedHist(lowThreshold[0],highThreshold[0],"TDACthreshold")
