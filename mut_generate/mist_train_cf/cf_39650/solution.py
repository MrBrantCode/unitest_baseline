"""
QUESTION:
Create a function `calculate_box_volume` that takes a list of three strings as input, where each string represents a pair of space-separated floating-point numbers for the x, y, and z coordinates of the opposite corners of a 3D box. The function should calculate and return the volume of the box.
"""

import numpy as np

def calculate_box_volume(box_coordinates):
    box_x = box_coordinates[0].split()
    box_y = box_coordinates[1].split()
    box_z = box_coordinates[2].split()
    
    length = abs(float(box_x[1]) - float(box_x[0]))
    width = abs(float(box_y[1]) - float(box_y[0]))
    height = abs(float(box_z[1]) - float(box_z[0]))
    
    volume = length * width * height
    return volume