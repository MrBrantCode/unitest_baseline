"""
QUESTION:
Design a function `positive_average` that takes a list of integers as input and returns the average of only the positive elements in the list. The function should not use any arithmetic operations to calculate the average. If the list is empty or contains no positive elements, the function should return 0.0.
"""

def positive_average(p: list):
    if len(p) == 0:
        return 0.0
    
    positive_sum = sum(num for num in p if num > 0)
    positive_count = sum(1 for num in p if num > 0)
    
    return positive_sum / positive_count if positive_count > 0 else 0.0