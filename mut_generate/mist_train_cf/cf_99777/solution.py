"""
QUESTION:
Write a function named `calculate_average` that calculates the average marks of a class given a list of marks. The function should take one argument, a list of marks, and return the average mark.
"""

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average