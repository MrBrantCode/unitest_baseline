"""
QUESTION:
Implement a function `filter_strings(data, n)` that takes an array of strings `data` and an integer `n` as input and returns a new array containing the strings with length greater than `n` and at least one uppercase letter. The function should maintain the order of the original array and have a time complexity of O(n), where n is the total number of characters in the input array. The solution should not use any built-in functions or regular expressions for checking uppercase letters.
"""

def filter_strings(data, n):
    def has_uppercase(string):
        for char in string:
            if 'A' <= char <= 'Z':
                return True
        return False
    
    result = [string for string in data if len(string) > n and has_uppercase(string)]
    return result