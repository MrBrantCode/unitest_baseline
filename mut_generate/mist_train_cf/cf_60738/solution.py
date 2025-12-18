"""
QUESTION:
Given the function name `count_unique_laminae` and a maximum number of tiles `max_tiles`, write a function to calculate the number of unique square laminae configurations that can be created. A square lamina is a square contour with a square "void", ensuring the figure maintains both vertical and horizontal symmetry. The function should take into account that the "core" square size must be less than the number of tiles and that the surrounding layer of tiles can occupy "odd" or "even" values. The function should return the total number of unique laminae that could be created with up to `max_tiles` tiles.
"""

import math

def count_unique_laminae(max_tiles):
    max_core_size = int(math.sqrt(max_tiles))
    
    lamina_count = 0
    
    for core_size in range(1, max_core_size+1):
        max_core_with_layers = int(math.sqrt(max_tiles + core_size**2))
        additional_layers = (max_core_with_layers - core_size) // 2
        lamina_count += additional_layers
    
    return lamina_count