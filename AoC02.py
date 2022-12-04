 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:47:23 2022 

@author: ptroll 
"""

file1 = open('/home/ubuntu/aoc22/aoc02.txt', 'r')
Lines = file1.readlines()

total = 0
# Strips the newline character
for line in Lines:
    game = str(line.strip())
    #print(game)
    if game == 'A X':
        total = total + 3 + 1
    if game == 'B Y':
        total = total + 3 + 2
    if game == 'C Z':
        total = total + 3 + 3
    if game == 'A Y':
        total = total + 6 + 2
    if game == 'B Z':
        total = total + 6 + 3
    if game == 'C X':
        total = total + 6 + 1
    if game == 'A Z':
        total = total + 0 + 3
    if game == 'B X':
        total = total + 0 + 1
    if game == 'C Y':
        total = total + 0 + 2

print(total)

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

total = 0
# Strips the newline character
for line in Lines:
    game = str(line.strip())
    #print(game)
    if game == 'A X':
        total = total + 0 + 3
    if game == 'B Y':
        total = total + 3 + 2
    if game == 'C Z':
        total = total + 6 + 1
    if game == 'A Y':
        total = total + 3 + 1
    if game == 'B Z':
        total = total + 6 + 3
    if game == 'C X':
        total = total + 0 + 2
    if game == 'A Z':
        total = total + 6 + 2
    if game == 'B X':
        total = total + 0 + 1
    if game == 'C Y':
        total = total + 3 + 3

print(total)
