"""
QUESTION:
Function Name: minCostToMoveChips
Information: Given an array of unique chip positions, determine the least expense to relocate all chips to a uniform location, where moving a chip to position[i] + 2 or position[i] - 2 incurs a cost of 0, and moving to position[i] + 1 or position[i] - 1 incurs a cost of i mod 3, with the cost doubled if the target position already has a chip.
Restrictions: 1 <= position.length <= 100, 1 <= position[i] <= 10^9.
"""

def minCostToMoveChips(position):
    even = sum(i % 2 == 0 for i in position)
    odd = sum(i % 2 != 0 for i in position)
    return min(even, odd)