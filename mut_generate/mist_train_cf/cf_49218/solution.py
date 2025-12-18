"""
QUESTION:
Design a function `calculate_attributes` that calculates the total volume and surface area of a list of 3D shapes. Each shape is represented by a dictionary containing attributes 'radius', 'height', and 'shape', where 'shape' can be 'cylinder', 'sphere', or 'cone'. The function should handle missing or incorrect information and return two lists, one for volumes and one for surface areas. The input list of shapes is expected to be in the format `[{'shape': 'shape_name', 'radius': radius_value, 'height': height_value}]`.
"""

import math

def calculate_attributes(shapes):
    volumes = []
    areas = []

    for shape in shapes:
        shape_type = shape.get('shape')
        r = shape.get('radius')
        h = shape.get('height')

        if not shape_type or not r:
            continue

        if shape_type.lower() in ['cylinder', 'cone'] and not h:
            continue

        if shape_type.lower() == 'cylinder':
            v = math.pi * math.pow(r, 2) * h
            a = 2 * math.pi * r * (r + h)

        elif shape_type.lower() == 'sphere':
            v = 4/3 * math.pi * math.pow(r, 3)
            a = 4 * math.pi * math.pow(r, 2)

        elif shape_type.lower() == 'cone':
            v = 1/3 * math.pi * math.pow(r, 2) * h
            a = math.pi * r * (r + math.sqrt(math.pow(r, 2) + math.pow(h, 2)))

        else:
            continue

        volumes.append(v)
        areas.append(a)

    return volumes, areas