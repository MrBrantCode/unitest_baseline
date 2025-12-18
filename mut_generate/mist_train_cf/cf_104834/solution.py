"""
QUESTION:
Create a function named `compute_max_difference` that takes two lists of numbers, `list1` and `list2`, and returns the maximum absolute difference between any two numbers from these lists. The absolute difference between two numbers is the absolute value of their difference.
"""

def compute_max_difference(list1, list2):
    max_diff = None
    for num1 in list1:
        for num2 in list2:
            diff = abs(num1 - num2)
            if max_diff is None or diff > max_diff:
                max_diff = diff
    return max_diff