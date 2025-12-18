"""
QUESTION:
Write a function `sort_list` that takes a list of dictionary objects as input, each containing "age" and "name" fields, and returns the list sorted in descending order by "age" and then ascending order by "name" for dictionary objects where "age" is 30 or more. The function should have a time complexity of O(n log n) and a space complexity of O(1), and should be implemented in a single line of code.
"""

def sort_list(lst):
    return sorted(filter(lambda x: x['age'] >= 30, lst), key=lambda x: (-x['age'], x['name']))