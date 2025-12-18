"""
QUESTION:
Write a function `check_result(n, listInt)` that takes two arguments, an integer `n` and a list of integers `listInt`. The function should multiply each element of `listInt` by `n`, check if the result is greater than 100, and return a new list containing the original numbers that meet this condition. The function must use list comprehensions.
"""

def check_result(n, listInt):
    return [i for i in listInt if i * n > 100]