"""
QUESTION:
Write a function minimal_swaps_to_palindrome(s) that determines if a given string of alphanumeric characters can be rearranged to form a palindrome and returns the minimum number of swaps needed. The function should ignore non-alphanumeric characters and be case insensitive. If it is impossible to create a palindrome from the given string, the function should return -1. The input string s can be empty or null, in which case the function should return -1 or an error message.
"""

import re
from collections import Counter

def minimal_swaps_to_palindrome(s):
    # Check if string is empty or null
    if not s:
        return "Invalid input. String is null or empty."
    
    # Ignore non-alphanumeric characters and convert to lower case
    s = re.sub(r'\W+', '', s).lower()
    
    # Count frequency of each character
    freqs = Counter(s)
    
    # Count number of characters with odd frequency
    odds = sum(count % 2 for count in freqs.values())
    
    # If more than 1 character has odd frequency, it's impossible to form a palindrome
    if odds > 1:
        return -1
    
    # Calculate the number of swaps
    chars = list(s)
    i, j = 0, len(s)-1
    swaps = 0
    
    while i < j:
        if chars[i] != chars[j]:
            k = j
            while i < k and chars[i] != chars[k]:
                k -= 1
            if i == k:  # chars[i] is the char with odd frequency
                chars[i], chars[i+1] = chars[i+1], chars[i]
                swaps += 1
            else:
                chars[k], chars[j] = chars[j], chars[k]
                swaps += j - k
        else:
            i += 1
            j -= 1
    
    return swaps