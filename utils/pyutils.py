import ROOT
import os
import csv
from array import array
from bisect import bisect_left

def column(matrix,i):
    #returns the ith column in matrix
    return [row[i] for row in matrix]

def floatList(array):
    #converts each element in a 1D array to float
    return [float(i) for i in array]

def extractCSV(path):
    #obtains data in an array given a valid path
    with open(path) as file:
        data = list(csv.reader(file))
    return data

def splitData(data,intervals):
    #given a 1D array and a list of intervals in the format
    #[[1 start, 1 end],[2 start, 2 end], ...],
    #outputs split data in the format 
    #[[1 interval],[2 interval], ...].
    splitData = []

    for x in range(len(intervals)):
        splitData.append(data[intervals[x][0]:intervals[x][1]])

    return splitData

def getMin(*args):
    #given lists, returns the minimum value
    return min([item for sublist in args for item in sublist])

def getMax(*args):
    #given lists, returns the maximum value
    return max([item for sublist in args for item in sublist])

def offSet(array,offset):
    #given a numeric array, adds offset to all entries
    for i in range(len(array)):
        array[i] = array[i] + offset

    return array

def scale(array,num):
    #given a numeric array, multiplies by scale to all entires
    for i in range(len(array)):
        array[i] = array[i] * num
    
    return array

def closest(array,num):
    #given a sorted array, returns index of closest value
    pos = bisect_left(array,num)
    if pos == 0:
        return 0
    if pos == -1:
        return len(array)-1
    return pos-1

def linApprox(x1,y1,x2,y2,x):
    #returns the linear approximation at x given two points (x1,y1) and (x2,y2).
    return (x-x1)*(y2-y1)/(x2-x1)+y1 
