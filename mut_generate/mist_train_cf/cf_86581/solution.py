"""
QUESTION:
Create a function named `filter_strings` that takes an array of strings `data` and an integer `n` as input. Return a new array containing the strings from `data` that have a length greater than `n` and at least one uppercase letter, in the original order. The function should have a time complexity of O(n), where n is the total number of characters in the input array. Do not use built-in functions or regular expressions to check for uppercase letters.
"""

def filter_strings(data, n):
    result = []
    
    for string in data:
        if len(string) > n and has_uppercase(string):
            result.append(string)
    
    return result

def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    
    return False