"""
QUESTION:
Write a function `remove_and_rearrange(lst)` that takes a non-empty list of integers, removes all elements with value 3, and rearranges the remaining elements so that all even numbers appear before odd numbers. The solution should be implemented in a single pass with a time complexity of O(n), where n is the length of the input list, and without using built-in functions like `filter()` or `list comprehension`.
"""

def remove_and_rearrange(lst):
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            lst.pop(i)
        else:
            i += 1
    i = 0
    j = len(lst) - 1
    while i < j:
        if lst[i] % 2 == 0:
            i += 1
        elif lst[j] % 2 == 1:
            j -= 1
        else:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    return lst