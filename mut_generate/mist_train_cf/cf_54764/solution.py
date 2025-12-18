"""
QUESTION:
Write a function `maxPointsInsideSquare(points, s)` that takes in a list of points `points` on a 2D plane and a side length `s` of a square grid, and returns a list containing the maximum number of points that are within or lie on any square grid of side length `s` and the coordinates of the square grid's center that contains the maximum points.

The input `points` is a list of lists, where each sublist contains two integers representing the x and y coordinates of a point. The input `s` is an integer representing the side length of the square grid. The function should return a list containing two elements: an integer representing the maximum number of points and a list of two integers representing the coordinates of the square grid's center.

Constraints: `1 <= len(points) <= 100`, `points[i].length == 2`, `-10^4 <= points[i][0], points[i][1] <= 10^4`, `1 <= s <= 5000`.
"""

def maxPointsInsideSquare(points, s):
    maxPoints = 0
    maxSquareCenter = None
    for point1 in points:
        for point2 in points:
            center = [(point1[0]+point2[0])/2, (point1[1]+point2[1])/2]
            left, right = center[0]-s/2, center[0]+s/2
            down, up = center[1]-s/2, center[1]+s/2
            count = 0
            for point in points:
                if left <= point[0] <= right and down <= point[1] <= up:
                    count += 1
            if count > maxPoints:
                maxPoints = count
                maxSquareCenter = center
    return [maxPoints, maxSquareCenter]