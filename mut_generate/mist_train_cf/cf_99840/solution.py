"""
QUESTION:
Write a function called `find_average` that takes a list of integers as input and returns the average of the integers in the list. The function should calculate the average by dividing the sum of the integers by the total count of integers.
"""

def find_average(arr):
    return sum(arr) / len(arr)