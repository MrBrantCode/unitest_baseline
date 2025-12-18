"""
QUESTION:
Create a function called `remove_duplicates_palindromes` that takes an array of strings as input, removes all duplicates while preserving the original order, and only keeps strings that are palindromes. The function should not use any additional libraries.
"""

def remove_duplicates_palindromes(arr):
    result = []
    seen = set()
    
    for word in arr:
        if word == word[::-1] and word not in seen:
            result.append(word)
            seen.add(word)
    
    return result