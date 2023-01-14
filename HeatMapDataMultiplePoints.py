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
pointToHit = numpy.array([[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]], dtype=int)
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
    count = int(pointToHit.size/2)
    hitArray = numpy.zeros(shape=(maxStep+1, count))
    ind = 0
    for step in numpy.arange(maxStep):
        positionsArray[step+1, ] = positionsArray[step, ] + singleStep()
        while ind < count:
            if hitCheck(pointToHit[ind], positionsArray[step+1, ]):
                hitArray[step+1, ind] = True
                ind += 1
            else:
                hitArray[step+1, ind] = False
                ind += 1
    return hitArray


def writeToCSV(hitArray):
    topic = "Suche nach folgenden Punkten:", pointToHit.tolist()
    header = "1 means hit, 0 means no hit"
    filename = "Search_For_Points_.csv"
    with open(filename, 'w') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(header)
        csvWriter.writerow(topic)
        csvWriter.writerows(hitArray)


def main():
    writeToCSV(walkTillHit(1, 80))


if __name__ == "__main__":
    main()
