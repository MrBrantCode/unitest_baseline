"""
QUESTION:
Create a function called `transformArray` that takes an array of integers as input. The function should return a nested object where each key is the index of the original array and each value is an object with two properties: "value" and "square". The "value" property should hold the value at the corresponding index in the array, and the "square" property should hold the square of the value.
"""

def transformArray(arr):
    return {index: {"value": value, "square": value ** 2} for index, value in enumerate(arr)}