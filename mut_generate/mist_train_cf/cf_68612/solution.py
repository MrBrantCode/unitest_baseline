"""
QUESTION:
Create a function `maxWidthOfVerticalArea(points)` that takes a list of points `points` as input, where each point is a list of two integers representing the x and y coordinates. The function should return the maximum width of the vertical area between two points such that no other point falls within this area. The input list `points` has a length `n` where `2 <= n <= 10^5`, and each point has two coordinates `xi` and `yi` where `0 <= xi, yi <= 10^9`.
"""

def maxWidthOfVerticalArea(points):
    points.sort()
    return max(points[i + 1][0] - points[i][0] for i in range(len(points) - 1))