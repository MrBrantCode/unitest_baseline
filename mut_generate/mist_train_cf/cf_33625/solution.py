"""
QUESTION:
Write a function named `format_point` that takes in eight parameters (`cx`, `cy`, `point_radius`, `sx`, `sy`, `ex`, `ey`, `count`) and returns a formatted string and an updated count.

The function should format the string according to the template: 
'1 4 0 1 0 0 50 -1 20 0.000 1 0.0000 {cx} {cy} {point_radius} {point_radius} {sx} {sy} {ex} {ey}'.
The count should be incremented by 1 after each function call.

Restrictions:
- `cx`, `cy`, `point_radius`, `sx`, `sy`, `ex`, `ey`, `count` are integers.
- The function should return a string and an integer.
"""

def format_point(cx, cy, point_radius, sx, sy, ex, ey, count):
    formatted_point = '1 4 0 1 0 0 50 -1 20 0.000 1 0.0000 {cx} {cy} {point_radius} {point_radius} {sx} {sy} {ex} {ey}'.format(**locals())
    count += 1
    return formatted_point, count