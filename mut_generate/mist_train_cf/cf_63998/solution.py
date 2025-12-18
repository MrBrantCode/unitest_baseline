"""
QUESTION:
Given the positions of n chips and a list of restricted positions, write a function minCostToMoveChips(position, restricted) that returns the minimum cost needed to move all the chips to the same position. The chips can be moved in one step to position[i] + 2 or position[i] - 2 with a cost of 0, and to position[i] + 1 or position[i] - 1 with a cost of 1. If it is not possible to move all chips to the same position due to restrictions, return -1.

The function should take as input two lists: position and restricted, where position is the list of chip positions and restricted is the list of restricted positions. The function should return the minimum cost as an integer.

The length of the position list is between 1 and 100, and the length of the restricted list is between 0 and 100. The chip positions and restricted positions are integers between 1 and 10^9.
"""

def minCostToMoveChips(position, restricted):
    from collections import Counter
    restricted = set(restricted)
    counter = Counter(position)
    min1, min2 = sorted(counter, key = counter.get)[:2]
    total_cost1, total_cost2 = 0, 0
    for p in counter:
        total_cost1 += counter[p] * ((abs(p - min1)) % 2) # `% 2` to account for the free moves of 2
        total_cost2 += counter[p] * ((abs(p - min2)) % 2)
    # Check and return the minimum cost, considering restrictions.
    if min1 not in restricted:
        return total_cost1
    elif min2 not in restricted:
        return total_cost2
    else:
        return -1