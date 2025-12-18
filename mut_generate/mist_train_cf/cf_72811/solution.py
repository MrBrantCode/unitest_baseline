"""
QUESTION:
Create a function named `rotate` that takes a list of numbers and an integer index as input, and returns a new list that is a clockwise rotation of the input list by the specified index. The function should not modify the original list. The rotation is performed by moving the last `idx` elements of the list to the front, and the first elements up to `idx` to the end.
"""

def rotate(lst, idx):
    return lst[-idx:] + lst[:-idx]