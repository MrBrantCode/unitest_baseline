"""
QUESTION:
Write a function `double_list` that doubles each element in the input list `lst` with a time complexity of O(n), where n is the length of the input list, and space complexity of O(1). The function should be implemented in a single line using list comprehension.
"""

def double_list(lst):
    """Doubles each element in the input list with a time complexity of O(n) and space complexity of O(n)."""
    return [(x * 2) for x in lst]