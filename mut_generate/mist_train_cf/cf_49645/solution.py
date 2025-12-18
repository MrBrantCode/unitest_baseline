"""
QUESTION:
Write a function `oceanViewAndSunlightExposure(heights, widths)` that takes two lists of integers `heights` and `widths` representing the heights and widths of buildings in a line, and returns a sorted list of indices (0-indexed) of buildings that have both an ocean view and sunlight exposure. 

The function should work under the constraints that `1 <= heights.length, widths.length <= 10^5` and `1 <= heights[i], widths[i] <= 10^9`. The ocean is to the right of the buildings, and a building has an ocean view if all the buildings to its right have a smaller height, and has sunlight exposure if there are no buildings to its left that are taller and wider than it.
"""

def oceanViewAndSunlightExposure(heights, widths):
    n = len(heights)
    buildings = []
    max_height = heights[n-1]
    max_width = widths[n-1]
    for i in range(n-1, -1, -1):
        if heights[i] >= max_height and widths[i] >= max_width:
            buildings.append(i)
            max_height = heights[i]
            max_width = widths[i]
    return sorted(buildings)