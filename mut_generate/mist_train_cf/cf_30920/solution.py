"""
QUESTION:
Write a function `determine_mode` that takes the current mode of a Color Sensor and the desired brightness levels for three lights as input, and returns the resulting mode after setting the brightness levels. The modes are represented by integers: 0 for color detection mode and 1 for light up mode. The function should take four parameters: `current_mode`, `light_1`, `light_2`, and `light_3`, all integers. If all brightness levels are 0, return 0. If the current mode is 0 and any brightness level is non-zero, return 1. Otherwise, return the current mode.
"""

def determine_mode(current_mode, light_1, light_2, light_3):
    if light_1 == 0 and light_2 == 0 and light_3 == 0:
        return 0  
    if current_mode == 0 and (light_1 > 0 or light_2 > 0 or light_3 > 0):
        return 1  
    return current_mode  