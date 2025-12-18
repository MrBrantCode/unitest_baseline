"""
QUESTION:
Implement a `BrachioGraph` class with attributes `inner_arm`, `outer_arm`, and `bounds`, and methods `set_bounds(x_min, y_min, x_max, y_max)`, `move_to(x, y)`, and `draw_line(x, y)`. The `set_bounds` method sets the drawing area bounds. The `move_to` and `draw_line` methods move the robot's drawing point to the specified coordinates within the drawing area, ensuring that the robot's arms do not extend beyond the bounds and do not intersect with each other. The robot's position is updated after each movement.
"""

def BrachioGraph(inner_arm, outer_arm, bounds):
    position = [0, 0]
    bounds_list = list(bounds)

    def set_bounds(x_min, y_min, x_max, y_max):
        bounds_list[0] = x_min
        bounds_list[1] = y_min
        bounds_list[2] = x_max
        bounds_list[3] = y_max

    def move_to(x, y):
        x_min, y_min, x_max, y_max = bounds_list
        x = max(x_min, min(x, x_max))
        y = max(y_min, min(y, y_max))
        position[0] = x
        position[1] = y

    def draw_line(x, y):
        x_min, y_min, x_max, y_max = bounds_list
        x = max(x_min, min(x, x_max))
        y = max(y_min, min(y, y_max))
        position[0] = x
        position[1] = y

    return set_bounds, move_to, draw_line