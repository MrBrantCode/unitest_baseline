"""
QUESTION:
Write a function `flatten_and_sum` that takes a nested list of integers as input, where the list can contain integers and lists, and can have up to four levels of nesting. The function should return the sum of all the integers within the nested lists. The function should be able to handle cases where the nested lists are not provided in a consistent manner and should have a time complexity of O(n), where n is the total number of elements in the input list.
"""

def flatten_and_sum(lst):
    total_sum = 0

    def helper(lst):
        nonlocal total_sum
        for item in lst:
            if isinstance(item, int):
                total_sum += item
            elif isinstance(item, list):
                helper(item)

    helper(lst)
    return total_sum