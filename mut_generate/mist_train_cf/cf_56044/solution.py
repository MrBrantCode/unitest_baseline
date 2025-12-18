"""
QUESTION:
Write a function `third_smallest` that takes a list of numbers (integers, floating point numbers, and negative integers) and returns the third smallest unique number. The list contains at least three unique numbers and has a variable length. The function should be able to handle negative numbers and floating point numbers.
"""

def third_smallest(numbers):
    return sorted(set(numbers))[2]