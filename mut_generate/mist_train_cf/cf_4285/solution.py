"""
QUESTION:
Write a function `filter_numeric_strings` that takes a list of strings as input and returns a list of integers. The function should include only numeric strings from the input list that have a value greater than 10, a length of 3 or less, and exclude any non-integer numeric strings. The output list should be sorted in descending order. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the length of the input list.
"""

def filter_numeric_strings(lst):
    return sorted([int(num) for num in lst if num.isdigit() and int(num) > 10 and len(num) <= 3], reverse=True)