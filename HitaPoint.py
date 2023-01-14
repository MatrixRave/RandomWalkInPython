#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:20:58 2022

@author: fabian
"""

import random as rd
import numpy
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
rd.seed(42)


# RandomWalk bis ein Punkt getroffen wird: Schleife läuft so lange, bis
# der vorgegebene Punkt getroffen wird! Als Ergebnis werden der Laufweg
# als Grafik und die benötigte Anzahl an Schritten ausgegeben
# der Punkt kann beliebig gewählt werden über eine Konsoleneingabe
# es bewegt sich immer nur ein Partikel auf der Karte
# die Anzahl der Würfe wird auf maximal 100.000 begrenzt dann bricht der Vorgan
# ab und der Versuch wird als Fehlerhaft gewertet.


numPart = 1
pointToHit = numpy.array([50, 50], dtype=int)
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


# speichervariable numpy.array der alle einzelnen schritte zugeordnet werden
# array als returntype
def walkTillHit(numPart=1, maxStep=5):
    # positionsArray wird direkt auf 0,0 als Startpunkt gesetzt
    positionsArray = numpy.zeros(shape=(maxStep+1, 2), dtype=int)
    for step in numpy.arange(maxStep):
        positionsArray[step+1, ] = positionsArray[step, ] + singleStep()
        if hitCheck(pointToHit, positionsArray[step+1, ]):
            tuple = (positionsArray, step+1, maxStep)
            return tuple
            break
    tuple = (positionsArray, step+1, maxStep)
    return tuple


def draw(tuple):
    print(tuple[0], pointToHit.shape)
    posArray = tuple[0]
    fig = go.Figure(data=go.Scatter(
        x=posArray[:tuple[1], 0],
        y=posArray[:tuple[1], 1],
        mode='markers',
        name='Walk till point is hit',
        marker=dict(
            color=numpy.arange(tuple[2]),
            size=5,
            colorscale='Reds',
            showscale=True)
        ))
    fig.add_trace(
        go.Scatter(
            x=posArray[tuple[1]:, 0],
            y=posArray[tuple[1]:, 1],
            mode='markers',
            marker_color='Black',
            hovertext=('Last point')))
    fig.show()


def main():
    draw(walkTillHit(1, 600))


if __name__ == "__main__":
    main()
