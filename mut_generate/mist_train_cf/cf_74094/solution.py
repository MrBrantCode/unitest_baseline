"""
QUESTION:
Design a function `longest_common_substring` that takes an array of strings `arr` and a positive integer `n` as input. The function should return the longest consecutive alphabetic substring that is common among all strings in `arr` and has a length of at least `n`. If there are multiple common substrings of the same maximum length, return the one that appears the most frequently across the strings. If the frequency is also the same, return the substring which appears first. The function should handle edge cases including when 'n' exceeds the length of the longest string in the array, and when there are no common substrings, and return `None` in such cases.
"""

from collections import Counter

def longest_common_substring(arr, n):
    # Store all possible substring in a list
    substrings = []
    for word in arr:
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                substrings.append(word[i:j])
                
    # Get all common substrings with length equal to or more than n
    c = Counter(substrings)
    common_substrings = [k for k, v in c.items() if v == len(arr) and len(k) >= n]
    
    # Handle the edge case when there are no common substrings
    if not common_substrings:
        return None
    
    # Get the longest common substrings
    max_length = max([len(s) for s in common_substrings])
    longest_substrings = [s for s in common_substrings if len(s) == max_length]
    
    # If there is only one longest common substring, return it
    if len(longest_substrings) == 1:
        return longest_substrings[0]
    
    # If there are multiple longest common substrings, return the one that appears most frequently
    frequency = Counter(longest_substrings)
    most_frequent_substrings = [k for k, v in frequency.items() if v == max(frequency.values())]
    
    if len(most_frequent_substrings) == 1:
        return most_frequent_substrings[0]
    
    # If the frequency is also the same, return the substring that appears first in the array
    for s in substrings:
        if s in most_frequent_substrings:
            return s