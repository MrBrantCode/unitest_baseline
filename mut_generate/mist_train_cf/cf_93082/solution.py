"""
QUESTION:
Create a function `compute_max_difference` that takes in two lists of numbers and returns the maximum absolute difference between any pair of numbers from the two lists. The absolute difference between two numbers is the absolute value of their difference. The function should handle lists of any length and contain any type of integer (positive, negative, or zero).
"""

def compute_max_difference(list1, list2):
    max_diff = None
    for num1 in list1:
        for num2 in list2:
            diff = abs(num1 - num2)
            if max_diff is None or diff > max_diff:
                max_diff = diff
    return max_diff