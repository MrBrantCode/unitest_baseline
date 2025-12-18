"""
QUESTION:
Write a function named `positive_average` that calculates the average of only the positive elements in a given list of integers without using basic arithmetic operations. The function should return the average as a floating-point number and handle cases where the input list contains no positive numbers.
"""

def positive_average(lst):
    positives = [num for num in lst if num > 0]
    return sum(positives) / len(positives) if positives else "No positive numbers in list"