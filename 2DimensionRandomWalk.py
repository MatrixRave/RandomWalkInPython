#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:59:19 2022

@author: fabian
"""
import random as rd
import numpy
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
rd.seed(42)

maxStep = 5
numPart = 1
NORTH = 1; SOUTH = 2; WEST = 3; EAST = 4


def singleStep():
    position = numpy.zeros(shape=(2,), dtype=int)
    currentStep = rd.randint(1, 4 + 1)
    position[1] += numpy.where(currentStep == NORTH, 1, 0)
    position[1] -= numpy.where(currentStep == SOUTH, 1, 0)
    position[0] += numpy.where(currentStep == EAST, 1, 0)
    position[0] -= numpy.where(currentStep == WEST, 1, 0)
    return position


def walkSteps(numPart=1, numstep=100):
    positionsArray = numpy.zeros(shape=(numstep+1, 2), dtype=int)
    for step in numpy.arange(numstep):
        positionsArray[step+1, ] = positionsArray[step, ] + singleStep()
    return positionsArray


def drawWalk(positionsArray):
    fig = go.Figure(data=go.Scatter(
        x=positionsArray[:, 0],
        y=positionsArray[:, 1],
        mode='markers',
        name='Randomwalk in 2 Dimensions',
        marker=dict(
            color=positionsArray,
            size=5,
            colorscale='Greens',
            showscale=True),
        line=dict(
            color='darkblue',
            width=1
        )
    ))
    fig.show()


def main():
    drawWalk(walkSteps(1, 50000))


if __name__ == "__main__":
    main()