"""
QUESTION:
Write a function `grayscaleToRGB` that takes an array of grayscale values as input, where each value ranges from 0 to 1. The function should return an array of corresponding RGB values, where each RGB value is an array of three integers ranging from 0 to 255, representing the red, green, and blue components of the color. The RGB values should be calculated using the formula: R = G = B = round(grayscale * 255).
"""

def grayscaleToRGB(grayscale_values):
    return [[round(value * 255)] * 3 for value in grayscale_values]