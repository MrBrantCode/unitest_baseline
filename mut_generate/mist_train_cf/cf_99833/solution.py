"""
QUESTION:
Write a function `find_most_unique_shape` that takes a list of dictionaries, each representing an object with keys 'weight', 'length', 'width', and 'height'. The function should return the object with the most unique shape, where uniqueness is calculated as the ratio of volume to surface area. The function should also print a message comparing the weight of the most unique shape to the average weight of all objects.
"""

import math

def find_most_unique_shape(objects):
    max_uniqueness = 0
    most_unique_shape = None
    total_weight = 0
    
    for obj in objects:
        weight = obj['weight']
        length = obj['length']
        width = obj['width']
        height = obj['height']
        
        volume = length * width * height
        surface_area = 2 * (length * width + length * height + width * height)
        uniqueness = volume / surface_area
        
        if uniqueness > max_uniqueness:
            max_uniqueness = uniqueness
            most_unique_shape = obj
        
        total_weight += weight
    
    avg_weight = total_weight / len(objects)
    
    if most_unique_shape['weight'] > avg_weight:
        print("The most unique shape is heavier than the average weight of all objects.")
    elif most_unique_shape['weight'] < avg_weight:
        print("The most unique shape is lighter than the average weight of all objects.")
    else:
        print("The most unique shape has the same weight as the average weight of all objects.")
    
    return most_unique_shape