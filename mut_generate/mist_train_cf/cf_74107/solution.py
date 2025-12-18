"""
QUESTION:
Design a function `is_point_in_cube(cube_origin, cube_size, point)` that takes as input the origin point of a cubic region `cube_origin` as a tuple of three integers, the size of the cube `cube_size` as an integer, and a 3D point `point` as a tuple of three integers. The function should return `True` if the point exists inside the boundaries of the cubic region and `False` otherwise.
"""

def entrance(cube_origin, cube_size, point):
    x_min, y_min, z_min = cube_origin
    x_max = x_min + cube_size
    y_max = y_min + cube_size
    z_max = z_min + cube_size

    x, y, z = point
    if x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max:
        return True
    else:
        return False