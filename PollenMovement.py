#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 00:36:51 2023

@author: fabian
"""
import numpy as np
import random as rd
import plotly.graph_objects as go


numpar = 1000
numStep = 100
NORTH = 1;  SOUTH = 2; WEST = 3; EAST = 4


def singleStep():
    position = np.zeros(shape=(2,), dtype=int)
    currentStep = rd.randint(1, 4 + 1)
    position[1] += np.where(currentStep == NORTH, 1, 0)
    position[1] -= np.where(currentStep == SOUTH, 1, 0)
    position[0] += np.where(currentStep == EAST, 1, 0)
    position[0] -= np.where(currentStep == WEST, 1, 0)
    return position


def walkSteps(numStep):
    positionsArray = np.zeros(shape=(numStep+1, 2), dtype=int)
    for step in np.arange(numStep):
        positionsArray[step+1, ] = positionsArray[step, ] + singleStep()
    return positionsArray


def generateParticles(numpar, numStep):
    particleArray = np.array()
    for step in np.arange(numpar):
        particleArray.append(walkSteps(numStep))
    return particleArray


def main():
    list = []
    list = (generateParticles(2, 10))
    print(list)
    print(np.shape(list))


if __name__ == "__main__":
    main()
