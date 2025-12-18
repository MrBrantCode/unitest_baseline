"""
QUESTION:
Calculate the sum of each row in a two-dimensional array, considering only positive numbers. The function should take a 2D list of integers as input and return a list of integers representing the sum of positive numbers in each row. The input array can contain both positive and negative integers.
"""

def row_sums(arr):
    return [sum([num for num in row if num > 0]) for row in arr]