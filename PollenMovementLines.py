#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:43:54 2023

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


def drawTraces(numpar, numStep):
    fig = go.Figure(data=go.Scatter(
        mode='markers',
        name='Draw pollen motion'))
    for step in np.arange(numpar):
        print(step)
        posArray = walkSteps(numStep)
        fig.add_trace(
            go.Scatter(
                x=posArray[:, 0],
                y=posArray[:, 1],
                marker=dict(
                    color=np.arange(numpar),
                    size=5,
                    colorscale='Greens',
                    showscale=False)))
    fig.show()


def main():
    drawTraces(500, 5000)


if __name__ == "__main__":
    main()
