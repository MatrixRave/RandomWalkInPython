#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:03:03 2022

@author: fabian
"""
import random as rd
import numpy
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
rd.seed(42)

np = 50000
ns = 10
NORTH = 1; SOUTH = 2; WEST = 3; EAST = 4; IN = 5; OUT = 6


def singleStep():
    position = numpy.zeros(shape=(3,), dtype=int)
    currentStep = rd.randint(1, 6 + 1)
    position[0] += numpy.where(currentStep == NORTH, 1, 0)
    position[0] -= numpy.where(currentStep == SOUTH, 1, 0)
    position[1] += numpy.where(currentStep == EAST, 1, 0)
    position[1] -= numpy.where(currentStep == WEST, 1, 0)
    position[2] += numpy.where(currentStep == OUT, 1, 0)
    position[2] -= numpy.where(currentStep == IN, 1, 0)
    return position


def walkSteps(numPart=1, numstep=100):
    positionsArray = numpy.zeros(shape=(numstep+1, 3), dtype=int)
    for step in numpy.arange(numstep):
        positionsArray[step+1, ] = positionsArray[step, ] + singleStep()
        tuple = (positionsArray, numstep)
    return tuple


def drawWalk(tuple):
    positionsArray = tuple[0]
    fig = go.Figure(data=go.Scatter3d(
        x=positionsArray[:, 0],
        y=positionsArray[:, 1],
        z=positionsArray[:, 2],
        mode='markers',
        name='Randomwalk in 2 Dimensions',
        marker=dict(
            color=numpy.arange(tuple[1]),
            size=5,
            colorscale='Greens',
            showscale=True),
        line=dict(
            color='darkblue',
            width=2
        )
    ))
    fig.show()


def main():
    drawWalk(walkSteps(1, 500000))


if __name__ == "__main__":
    main()
