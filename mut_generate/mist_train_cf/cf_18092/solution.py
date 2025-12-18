"""
QUESTION:
Write a function `get_elements(arr)` that takes an array of strings `arr` as input, and returns a sorted array of unique elements that are palindromes and end with the character 's', while maintaining a time complexity of O(n).
"""

def is_palindrome(s):
    return s == s[::-1]

def entrance(arr):
    seen = set()
    result = {}
    
    for element in arr:
        if element[-1] != 's' or not is_palindrome(element):
            continue
        seen.add(element)
        if element in result:
            continue
        result[element] = 1
    
    return sorted(result.keys())