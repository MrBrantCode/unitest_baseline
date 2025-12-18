"""
QUESTION:
Create a function `find_max` that takes a list of positive integers as input and returns the maximum value. The function should have a time complexity of O(n), where n is the length of the list.
"""

def find_max(lst):
    max_val = 0
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val