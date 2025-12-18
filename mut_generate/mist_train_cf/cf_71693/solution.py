"""
QUESTION:
Write a function `parallelogram_area` that takes a list of tuples as input, where each tuple contains two positive decimal values representing the base and height of a parallelogram in centimeters. The function should calculate the area of each parallelogram by multiplying the base by the height, round the result to 2 decimal places, and return a list of these areas. The function must be efficient enough to handle a large list of tuples (up to 10^6 tuples) with base and height values between 1.01 cm and 1000.53 cm.
"""

def parallelogram_area(lst):
    return [round(base * height, 2) for base, height in lst]