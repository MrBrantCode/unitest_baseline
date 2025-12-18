"""
QUESTION:
Given a list of unique chip positions, determine the minimum cost to relocate all chips to a single position. The cost of moving a chip is 0 if the move is from `position[i]` to `position[i] + 2` or `position[i] - 2`, and 1 if the move is to `position[i] + 1` or `position[i] - 1`. The function `minCostToMoveChips(position)` should take a list of integers `position` and return the minimum cost. The input is subject to the following constraints: `1 <= len(position) <= 100` and `1 <= position[i] <= 10^9`.
"""

def minCostToMoveChips(position):
    even_chips, odd_chips = 0, 0
    for i in position:
        if i % 2 == 0:
            even_chips += 1
        else:
            odd_chips += 1
    return min(even_chips, odd_chips)