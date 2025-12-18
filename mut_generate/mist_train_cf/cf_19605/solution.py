"""
QUESTION:
Write a function named `remove_duplicates_palindromes` that takes an array of strings as input. The function should return a new array containing only the unique palindromes from the input array, in the same order they appear. A palindrome is a string that reads the same backward as forward, such as "racecar" or "madam". The function should exclude any non-palindrome strings and duplicates from the output array.
"""

def remove_duplicates_palindromes(arr):
    seen = set()
    result = []
    
    for word in arr:
        if word == word[::-1] and word not in seen:
            result.append(word)
            seen.add(word)
    
    return result