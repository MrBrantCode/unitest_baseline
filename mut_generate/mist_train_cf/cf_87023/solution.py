"""
QUESTION:
Implement a function named `are_anagrams` that checks if two input strings are anagrams of each other. The function should be case-insensitive, ignore non-alphabetic characters, and have a time complexity of O(n log n). It should also use constant space complexity and handle strings with Unicode characters correctly. The function should not use any built-in sorting or comparison functions.
"""

import re

def are_anagrams(str1, str2):
    # Convert strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Remove non-alphabetic characters
    str1 = re.sub(r'[^a-z]', '', str1)
    str2 = re.sub(r'[^a-z]', '', str2)
    
    # Sort the characters of both strings
    sorted_str1 = quicksort(list(str1))
    sorted_str2 = quicksort(list(str2))
    
    # Compare the sorted strings character by character
    if len(sorted_str1) != len(sorted_str2):
        return False
    for i in range(len(sorted_str1)):
        if sorted_str1[i] != sorted_str2[i]:
            return False
    
    return True

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)