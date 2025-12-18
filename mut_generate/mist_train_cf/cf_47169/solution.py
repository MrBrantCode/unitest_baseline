"""
QUESTION:
Write a function `isRectangleCover(rectangles)` that takes an array of rectangles where `rectangles[i] = [xi, yi, ai, bi]` represents an axis-aligned rectangle with `(xi, yi)` as the bottom-left point and `(ai, bi)` as the top-right point. The function should return `true` if all the rectangles together form an exact cover of a rectangular region and its area, otherwise return the total area of all rectangles. Additionally, if any rectangle is entirely contained within another, return -1. 

Restrictions:
1 <= rectangles.length <= 2 * 10^4
rectangles[i].length == 4
-10^5 <= xi, yi, ai, bi <= 10^5
"""

def isRectangleCover(rectangles):
    events = []
    total_area = 0
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')

    for x1, y1, x2, y2 in rectangles:
        min_x, min_y = min(min_x, x1), min(min_y, y1)
        max_x, max_y = max(max_x, x2), max(max_y, y2)
        total_area += (x2 - x1) * (y2 - y1)

        events.append((x1, False, y1, y2))
        events.append((x2, True, y1, y2))

    events.sort()

    sweep_line_area = 0
    curr_min_y, curr_max_y = events[0][2], events[0][3]
    last_time = events[0][0]

    for event in events[1:]:
        if event[0] != last_time and curr_min_y < curr_max_y:
            if sweep_line_area > (max_x - min_x) * (curr_max_y - curr_min_y):
                return False

            if last_time >= min_x and event[0] <= max_x:
                sweep_line_area += (max_x - min_x) * (curr_max_y - curr_min_y)

            curr_min_y, curr_max_y = event[2], event[3]
        else:
            if event[1]:
                curr_max_y = max(curr_max_y, event[3])
            else:
                curr_min_y = min(curr_min_y, event[2])

        last_time = event[0]

    return total_area == sweep_line_area