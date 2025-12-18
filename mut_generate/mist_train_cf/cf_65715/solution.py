"""
QUESTION:
Given the function name minCostToMoveChips, compute the minimal expenditure required to consolidate chips to a single, uniform location. The function takes as input a list of chip positions (position) where 1 <= len(position) <= 100 and 1 <= position[i] <= 10^9. In a single maneuver, a chip can be moved to position[i] + 2 or position[i] - 2 at a cost of 0, or to position[i] + 1 or position[i] - 1 at a cost of 1, regardless of the actual position.
"""

def minCostToMoveChips(position):
    oddPlaces = sum(x % 2 for x in position)
    evenPlaces = len(position) - oddPlaces
    return min(oddPlaces, evenPlaces)