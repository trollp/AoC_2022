#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:28:24 2022 

@author: ptroll 
"""

# read file by lines
file1 = open('aoc22/aoc01.txt', 'r')
Lines = file1.readlines()

summary = 0
list = []
# Strips the newline character
for line in Lines:
    cal = str(line.strip())
    if len(cal) == 0:
        cal = 0
    cal = int(cal)
    summary = summary + cal
    if cal == 0:
        list.append(summary)
        summary = 0
list.sort()
print(max(list))
print(sum((list[-3:])))
