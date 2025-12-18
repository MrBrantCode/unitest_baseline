"""
QUESTION:
Write a function named `calculate_average` that takes a list of numbers as input and returns the average of the numbers. The average is calculated by dividing the sum of the numbers by the total count of numbers in the list.
"""

def calculate_average(lst):
    return sum(lst) / len(lst)