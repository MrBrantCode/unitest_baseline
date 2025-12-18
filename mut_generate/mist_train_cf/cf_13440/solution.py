"""
QUESTION:
Write a function `longest_strings` that takes an array of strings as input. The function should return a new array containing only the strings with the longest length. If there are multiple strings with the longest length, return all of them in the new array. The function should handle empty arrays and arrays containing only empty strings by returning an empty array and an array with all the empty strings respectively.
"""

def longest_strings(arr):
    if not arr:
        return []
    
    max_length = max(len(s) for s in arr)
    longest = [s for s in arr if len(s) == max_length]
    
    return longest