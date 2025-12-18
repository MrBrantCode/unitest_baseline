"""
QUESTION:
Write a function `maxDistance(arrays)` that takes in a list of `m` arrays, each of which is arranged in ascending order, and returns the greatest possible distance between two integers selected from two distinct arrays. The distance between two integers `a` and `b` is defined as their absolute difference `|a - b|`. The function must run in linear time complexity and use constant space complexity. 

`2 <= m <= 10^5`, `1 <= arrays[i].length <= 500`, `-10^4 <= arrays[i][j] <= 10^4`.
"""

def entrance(arrays):
    minVal, maxVal = arrays[0][0], arrays[0][-1]
    maxDistance = 0

    for array in arrays[1:]:
        maxDistance = max(maxDistance, abs(maxVal - array[0]), abs(minVal - array[-1]))
        minVal, maxVal = min(minVal, array[0]), max(maxVal, array[-1])
        
    return maxDistance