#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:43:18 2023

@author: fabian
"""
import random as rd
import numpy
import csv
rd.seed(42)




numPart = 1
pointToHit = numpy.array([4, 3], dtype=int)
NORTH = 1; SOUTH = 2; WEST = 3; EAST = 4


def hitCheck(pointToHit, realPoint):
    return numpy.array_equal(pointToHit, realPoint)


def singleStep():
    position = numpy.zeros(shape=(2,), dtype=int)
    currentStep = rd.randint(1, 4 + 1)
    position[1] += numpy.where(currentStep == NORTH, 1, 0)
    position[1] -= numpy.where(currentStep == SOUTH, 1, 0)
    position[0] += numpy.where(currentStep == EAST, 1, 0)
    position[0] -= numpy.where(currentStep == WEST, 1, 0)
    return position


def walkTillHit(numPart=1, maxStep=5):
    positionsArray = numpy.zeros(shape=(maxStep+1, 2), dtype=int)
    hitArray = numpy.zeros(shape=(maxStep+1, 2))
    for step in numpy.arange(maxStep):
        positionsArray[step+1, ] = positionsArray[step, ] + singleStep()
        if hitCheck(pointToHit, positionsArray[step+1, ]):
            hitArray[step+1, 0] = True
            hitArray[step+1, 1] = step+1
        else:
            hitArray[step+1, 0] = False
            hitArray[step+1, 1] = 0
    return hitArray


def writeToCSV(hitArray):
    print(hitArray)
    headers = ['Treffer', 'Nach Schritten']
    filename = "Search_For_Point_4,3_.csv"
    with open(filename, 'w') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(headers)
        csvWriter.writerows(hitArray)


def main():
    writeToCSV(walkTillHit(1, 50000))


if __name__ == "__main__":
    main()
