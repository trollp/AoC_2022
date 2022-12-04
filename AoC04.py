#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 09:42:02 2022 
@author: ptroll 
"""

# read file by lines
file1 = open('aoc04.txt', 'r')
Lines = file1.readlines()
    
total1 = 0
total2 = 0
# Strips the newline character
for line in Lines:
    line = str(line.strip())
    IDgroups = line.split(',')
    ID1 = IDgroups[0].split('-')
    ID2 = IDgroups[1].split('-')
    range1 = range(int(ID1[0]),int(ID1[1])+1)
    range2 = range(int(ID2[0]),int(ID2[1])+1)
# --- Part One ---
    if all(e in range1 for e in range2) or all(e in range2 for e in range1):
        total1 = total1 + 1
# --- Part Two ---
    if any(e in range1 for e in range2) or any(e in range2 for e in range1):
        total2 = total2 + 1
    
print('Part One: %s' %total1)
print('Part Two: %s' %total2)

