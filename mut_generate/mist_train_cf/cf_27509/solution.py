"""
QUESTION:
Write a function `calculate_color` that takes two parameters: 
- `s` (float): The brightness of the LED, ranging from 0.0 to 1.0.
- `sliders` (list of floats): The slider values for red, green, and blue components, each ranging from 0.0 to 1.0.

The function should return a tuple `(r, g, b)` representing the calculated RGB color values, where each value is an integer between 0 and 255. The RGB values are calculated by multiplying the corresponding slider value with 255 and the brightness `s`, and then rounding down to the nearest integer.
"""

import math

def calculate_color(s, sliders):
    r = int(sliders[0] * 255 * s)
    g = int(sliders[1] * 255 * s)
    b = int(sliders[2] * 255 * s)
    return (r, g, b)