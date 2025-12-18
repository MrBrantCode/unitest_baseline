"""
QUESTION:
Implement a function named `filter_strings` that takes an array of strings `data` and an integer `n` as input. The function should return a new array containing strings from `data` with a length greater than `n` and at least one uppercase letter, maintaining the original order.
"""

def filter_strings(data, n):
    result = []
    for string in data:
        if len(string) > n and any(char.isupper() for char in string):
            result.append(string)
    return result