"""
QUESTION:
Write a function `findMinArrowShots(points)` that takes a 2D list `points` of integers, where each sublist contains four integers representing the start and end coordinates of the horizontal diameter and the vertical diameter of a balloon in 3D space. The function should return the minimum number of arrows that must be shot to burst all balloons, with no limit to the number of arrows that can be shot. The input list `points` has the following restrictions: `0 <= points.length <= 10^4`, `points[i].length == 4`, `-2^31 <= xstart < xend <= 2^31 - 1`, and `-2^31 <= ystart < yend <= 2^31 - 1`.
"""

def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    end = points[0][1]
    arrows = 1

    for i in range(1, len(points)):
        if points[i][0] > end:
            arrows += 1
            end = points[i][1]

    return arrows