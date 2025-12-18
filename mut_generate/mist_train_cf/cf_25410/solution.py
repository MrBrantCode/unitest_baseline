"""
QUESTION:
Write a function named `transformArray` that takes an array of objects as input, where each object contains 'name' and 'age' properties. The function should return a new array of objects with the 'name' property unchanged and the 'age' property doubled.
"""

def transformArray(arr):
    return [{"name": obj["name"], "age": obj["age"] * 2} for obj in arr]