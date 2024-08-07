import csv, numpy as np, matplotlib.pyplot as plt

from polygon import polyPoints
#from sklearn.mixture import GaussianMixture


def col2num(col):
    #Excel-style string to number, e.g., A = 1, Z = 26, AA = 27, AAA = 703.
    n = 0
    for c in col:
        n = n * 26 + 1 + ord(c) - ord('A')

    return n

def excelSplit(s):
    #given an excel coordinate (ex. WQ211), returns the position within a list.
    head = s.rstrip('0123456789')
    tail = int(s[len(head):])

    return [tail-1,col2num(head)-1]

def excelCoords(path):
    #converts a csv file with each line representing the vetices of a polygon
    #to a raw list of coordinates inside all polygons
    finalData = []

    with open(path) as file:
        data = list(csv.reader(file))

    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            row.append(excelSplit(data[i][j]))

        finalData.extend(polyPoints(row))

    return finalData
