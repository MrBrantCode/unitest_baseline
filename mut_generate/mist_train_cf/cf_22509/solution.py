"""
QUESTION:
Write a function named `calculate_volume` that calculates the volume of a cuboid given its length, width, and height. The function should take three positive integers less than or equal to 10^9 as input, handle edge cases where the length, width, or height is equal to 1, and return the volume as a floating-point number rounded to two decimal places. The function should not use any built-in functions or libraries to calculate the volume.
"""

def calculate_volume(length, width, height):
    volume = length * width * height
    return round(volume, 2)