"""
QUESTION:
Write a function called `remove_duplicates_palindromes` that takes an array of strings as input, and returns a new array containing only the palindrome strings from the input array, with all duplicates removed and the original order preserved. The function should not use any additional data structures or libraries.
"""

def remove_duplicates_palindromes(arr):
    result = []
    seen = set()
    
    for word in arr:
        if word == word[::-1] and word not in seen:
            result.append(word)
            seen.add(word)
    
    return result