"""
QUESTION:
Write a function `positive_integers` that takes a list of integers as input and returns a new list containing only the positive integers from the input list. The function should have a time complexity of O(n) and should not use any built-in functions or libraries.
"""

def positive_integers(lst):
    result = []
    for num in lst:
        if num > 0:
            result.append(num)
    return result