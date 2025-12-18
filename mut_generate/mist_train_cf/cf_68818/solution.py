"""
QUESTION:
Write a function `FunctionB` that takes two lists of numbers `lst` and `lst2` as input and returns a list of unique numbers that are common in both lists and less than 50. The function should have an optimal time complexity.
"""

def FunctionB(lst, lst2):
    return list(set(num for num in set(lst) if num < 50 and num in set(lst2)))