"""
QUESTION:
Implement a function `closest_pair(points)` that takes a list of 2D points as input, where each point is represented as a tuple (x, y), and returns the two closest points in the list. The function should use the divide and conquer algorithm to efficiently find the closest pair of points. The input list can contain any number of points, and the function should handle the case where there are 3 or fewer points separately.
"""

import math

def closest_pair(points):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def brute_force(points):
        min_dist = float('inf')
        pair = ()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    pair = (points[i], points[j])
        return pair

    def closest_pair_recursive(sorted_x, sorted_y):
        n = len(sorted_x)
        if n <= 3:
            return brute_force(sorted_x)

        mid = n // 2
        mid_point = sorted_x[mid]
        left_x = sorted_x[:mid]
        right_x = sorted_x[mid:]

        left_y = [p for p in sorted_y if p[0] <= mid_point[0]]
        right_y = [p for p in sorted_y if p[0] > mid_point[0]]

        left_pair = closest_pair_recursive(left_x, left_y)
        right_pair = closest_pair_recursive(right_x, right_y)

        min_pair = left_pair if distance(left_pair[0], left_pair[1]) < distance(right_pair[0], right_pair[1]) else right_pair

        strip = [p for p in sorted_y if abs(p[0] - mid_point[0]) < distance(min_pair[0], min_pair[1])]
        strip_closest = brute_force(strip)

        return strip_closest if distance(strip_closest[0], strip_closest[1]) < distance(min_pair[0], min_pair[1]) else min_pair

    sorted_x = sorted(points, key=lambda x: x[0])
    sorted_y = sorted(points, key=lambda x: x[1])

    return closest_pair_recursive(sorted_x, sorted_y)