"""
QUESTION:
Create a function `mine_gold` that takes a dictionary `goldMines` where the keys are the names of gold mines and the values are tuples representing the coordinates of the mines, and a tuple `centralHub` representing the coordinates of the central hub. The function should sort the gold mines based on their proximity to the central hub and extract the maximum amount of gold while maintaining a minimum distance of 20 units between the central hub and any gold mine. The function should return the total gold extracted and the distance traveled from the central hub. The function should assume that each gold mine has 10 units of gold.
"""

import math

def mine_gold(goldMines, centralHub):
    # sort the gold mines based on their proximity to the central hub
    goldMines = dict(sorted(goldMines.items(), key=lambda x: math.sqrt((centralHub[0]-x[1][0])**2 + (centralHub[1]-x[1][1])**2)))
    
    # extract the maximum amount of gold while maintaining a minimum distance of 20 units between the central hub and any gold mine
    totalGold = 0
    distanceTraveled = 0
    for mine in goldMines:
        if math.sqrt((centralHub[0]-goldMines[mine][0])**2 + (centralHub[1]-goldMines[mine][1])**2) >= 20:
            totalGold += 10
            distanceTraveled += math.sqrt((centralHub[0]-goldMines[mine][0])**2 + (centralHub[1]-goldMines[mine][1])**2)
    
    return totalGold, distanceTraveled