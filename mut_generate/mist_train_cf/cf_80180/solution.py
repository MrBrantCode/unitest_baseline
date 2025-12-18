"""
QUESTION:
Design a function called `total_volume` that calculates the total volume of a list of 3D objects. Each object is represented by a dictionary containing 'radius', and either 'height' (for cylinders) or not (for spheres), along with an 'object_type' to distinguish between them. The function should be able to handle a list of both cylinders and spheres.
"""

import math

def calculate_cylinder_volume(radius, height):
  return math.pi * math.pow(radius, 2) * height

def calculate_sphere_volume(radius):
  return 4/3 * math.pi * math.pow(radius, 3)

def total_volume(objects):
  total_volume = 0
  for obj in objects:
    object_type = obj.get('object_type')
    if object_type == 'cylinder':
      total_volume += calculate_cylinder_volume(obj['radius'], obj['height'])
    elif object_type == 'sphere':
      total_volume += calculate_sphere_volume(obj['radius'])
  return total_volume