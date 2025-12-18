"""
QUESTION:
Remove all duplicates from an array of strings while preserving the order of the elements, and only include strings that are palindromes.

Implement a function `remove_duplicates_palindromes(arr)` that takes an array of strings as input and returns the resulting array of unique palindrome strings in the original order.
"""

def remove_duplicates_palindromes(arr):
    seen = set()
    result = []
    
    for word in arr:
        if word == word[::-1] and word not in seen:
            result.append(word)
            seen.add(word)
    
    return result