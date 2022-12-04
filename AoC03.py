#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 08:28:24 2022 
@author: ptroll 
"""

# read file by lines
file1 = open('aoc03.txt', 'r')
Lines = file1.readlines()

total = 0
# Strips the newline character
for line in Lines:
    line = str(line.strip())
    #print(len(line))
    half = int((len(line)+1)/2)
    pack1 = line[0:half]
    pack2 = line[half:half*2]
    item=list(set(pack1)&set(pack2))[0]
    print(item)
    if item.islower():
        total = total + (ord(item) - 96)
    if item.isupper():
        total = total + (ord(item) - 38)
print(total)

#--- Part Two ---

total = 0
# Strips the newline character
for i in range(0,len(Lines),3):
    rucksack1 = str(Lines[i].strip())
    rucksack2 = str(Lines[i+1].strip())
    rucksack3 = str(Lines[i+2].strip())
    item=list(set(rucksack1)&set(rucksack2)&set(rucksack3))[0]
    print(item)
    if item.islower():
        total = total + (ord(item) - 96)
    if item.isupper():
        total = total + (ord(item) - 38)
print(total)
