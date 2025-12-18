"""
QUESTION:
You are given an array `points` and an array `obstacles` where `points[i] = [xi, yi]` and `obstacles[i] = [oxi, oyi]` denote integral coordinates on the X-Y plane. You are also given your `location = [posx, posy]` and an integer `angle`. 

Write a function `visiblePoints(self, points, obstacles, angle, location)` that returns the maximum number of points you can see. The function should consider that you are facing directly east from your position and your field of view in degrees is represented by `angle`. Points at the same location as you can always be seen, and obstacles obstruct your vision to other points.
"""

import bisect, math
from collections import Counter

def visiblePoints(points, obstacles, angle, location):
    points_views, obstacle_views = [], []
    same, res, max_val = 0, 0, 0
    for point in points: 
        if point == location: 
            same += 1 
        else: 
            degree = math.degrees(math.atan2(point[1] - location[1], point[0] - location[0]))
            points_views.append(degree)
    for obstacle in obstacles: 
        degree = math.degrees(math.atan2(obstacle[1] - location[1], obstacle[0] - location[0]))
        obstacle_views.append(degree)
    all_views = sorted(points_views)
    counter = Counter(obstacle_views)
    all_views = all_views + [view + 360 for view in all_views] 
    for i in range(len(all_views)): 
        if i > 0 and all_views[i] - 360 == all_views[i - 1]: 
            same -= 1 
        else: 
            same = 0
        while all_views[i] - all_views[res] > angle: 
            if all_views[res] in counter and counter[all_views[res]] > 0: 
                same -= 1
            res += 1
        max_val = max(max_val, i - res + 1 - same)
    return max_val + same