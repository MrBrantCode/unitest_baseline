"""
QUESTION:
Write a function `reverse_and_remove_duplicates(s)` that takes a string `s` as input, reverses it in place without using any additional data structures, and removes all duplicate characters. The function should have a time complexity of O(n) and a space complexity of O(1) is not feasible due to the use of a set for duplicate removal, however the function can have a space complexity of O(n) where n is the number of unique characters in the string.
"""

def reverse_and_remove_duplicates(s):
    chars = list(s)
    
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    seen = set()
    unique_chars = []
    for char in chars:
        if char not in seen:
            seen.add(char)
            unique_chars.append(char)
    
    return ''.join(unique_chars)