'''
Converts the readouts from CMSIT text files to matrices 
'''


import os
import numpy


def txt2list(filePath):
    with open(filePath) as file:
    
        #final matrix. 1st index is the type, 2nd index is the row, 3rd index is the column
        #the raw text file is actually transposed - in the raw file, each column is actually the rows
        mymatrix = [[],[],[],[]]
    
        #matches each parameter to an index
        indexArray = [['ENABLE',0],['HITBUS',1],['INJEN',2],['TDAC',3]]

        for line in file:

            linelist = line.split()

            if len(linelist) > 0:
                for x in range(len(indexArray)):
                    if linelist[0] == indexArray[x][0]:
                        mymatrix[x].append([float(n) for n in linelist[1].split(",")])

    return mymatrix

def getEnable(matrix):
    return matrix[0]
