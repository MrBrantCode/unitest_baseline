"""
QUESTION:
Write a function `add_elements(list1, list2)` that takes two lists of integers as input, adds elements from `list1` to `list2` if they are divisible by 3, and returns the updated `list2` in ascending order.
"""

def add_elements(list1, list2):
    # Filter elements divisible by 3 using list comprehension
    # and add them to the second list
    list2 += [i for i in list1 if i % 3 == 0]

    # Sort the resulted list in ascending order
    list2.sort()
    
    return list2