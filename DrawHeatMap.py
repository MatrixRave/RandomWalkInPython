#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:25:52 2023

@author: fabian
"""
import csv

with open('Search_For_Points_.csv') as csv_datei:
    reader = csv.reader(csv_datei, delimiter=',')
    kopfzeile = next(reader)
    for item in csv_datei:
        print(item[56])
