"""
QUESTION:
Write a function named get_even_numbers that takes in a list of integers and returns a set containing only the even numbers. The function should validate that the input list is not empty and contains only positive integers, otherwise it should raise an exception. The function should be implemented using recursion and have a time complexity of O(n) where n is the length of the input list.
"""

def get_even_numbers(lst):
    if len(lst) == 0:
        raise Exception("Input list is empty")

    if any(num <= 0 for num in lst):
        raise Exception("Input list contains non-positive integers")

    if len(lst) == 1:
        if lst[0] % 2 == 0:
            return set(lst)
        else:
            return set()

    mid = len(lst) // 2
    left_set = get_even_numbers(lst[:mid])
    right_set = get_even_numbers(lst[mid:])
    return left_set.union(right_set)