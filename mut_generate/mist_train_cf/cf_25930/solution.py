"""
QUESTION:
Write a function named 'calculate_mean' that calculates the mean of a given list of numbers. The function should take a list of integers as input and return the mean value as a float.
"""

def calculate_mean(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum/len(lst)