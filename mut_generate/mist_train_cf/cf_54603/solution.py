"""
QUESTION:
Write a function `findRadius(houses, heaters)` that determines the minimum radius standard for the heaters, given the positions of `houses` and `heaters` on a horizontal line, such that all houses are covered by the heaters. The function should take in two lists of integers `houses` and `heaters`, representing the positions of houses and heaters respectively. The function should return the minimum radius standard. The input lists will have the following constraints: `1 <= len(houses), len(heaters) <= 3 * 10^4` and `1 <= houses[i], heaters[i] <= 10^9`.
"""

import bisect

def findRadius(houses, heaters):
    heaters.sort()
    answer = 0

    for house in houses:
        radius = float('inf')
        le = bisect.bisect_right(heaters, house)
        if le > 0:
            radius = min(radius, house - heaters[le-1])
        ge = bisect.bisect_left(heaters, house)
        if ge < len(heaters):
            radius = min(radius, heaters[ge] - house)
        answer = max(answer, radius)

    return answer