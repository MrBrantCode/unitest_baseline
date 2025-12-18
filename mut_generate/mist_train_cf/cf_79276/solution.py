"""
QUESTION:
Write a function named `dot_product` that takes two lists of integers as parameters. The function should calculate and return the dot product of these two vectors, assuming they have an equal number of integers. The function should handle edge cases where an input is empty or the lists have unequal lengths. Optimize the solution to handle lists with up to 1,000,000 elements.
"""

def dot_product(list1, list2):
    # Check if both lists are not empty and have the same length
    if list1 and list2 and len(list1) == len(list2):
        return sum(x*y for x, y in zip(list1, list2))
    else:
        return "Lists are empty or do not have the same length"