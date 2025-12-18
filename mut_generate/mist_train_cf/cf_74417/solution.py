"""
QUESTION:
Given an array of chip positions, write a function minCostToMoveChips(position) that calculates the minimum cost to move all chips to the same position, where the cost of moving a chip to position[i] + 1 or position[i] - 1 is i mod 3, and the cost of moving a chip to position[i] + 2 or position[i] - 2 is 0. The input array position has a length of at least 1 and at most 100, and each chip position is an integer between 1 and 10^9.
"""

def minCostToMoveChips(position):
    mod = [0, 0, 0]
    
    for i in position:
        mod[i % 3] += 1

    return min(mod[0]*2, mod[1], mod[2]*2)