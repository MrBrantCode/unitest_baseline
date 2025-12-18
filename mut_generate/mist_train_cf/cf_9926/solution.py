"""
QUESTION:
Write a function `longest_substring_without_repetition` that takes a string `s` as input and returns the length of the longest substring without any repeating characters. The function should use a sliding window approach and a set data structure to keep track of unique characters. The function should iterate through the string, updating the start and end pointers of the sliding window, and return the maximum length of the substring without repetition.
"""

def longest_substring_without_repetition(s):
    start = 0
    end = 0
    unique_chars = set()
    max_length = 0
    
    while end < len(s):
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            end += 1
            max_length = max(max_length, end - start)
        else:
            unique_chars.remove(s[start])
            start += 1
            
    return max_length