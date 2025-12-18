"""
QUESTION:
Create a function called `find_negatives` that takes a 2D array as input. The function should return a list of coordinate pairs (x, y) representing the row and column positions of the negative elements in the array. If there are no negative elements or if the array is empty, the function should return an empty list.
"""

def find_negatives(arr):
    return [(i, j) for i, row in enumerate(arr) for j, num in enumerate(row) if num < 0]