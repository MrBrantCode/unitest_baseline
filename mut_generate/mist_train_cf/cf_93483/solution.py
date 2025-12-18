"""
QUESTION:
Write a function `length_of_longest_substring(s)` to find the length of the longest substring without repeating characters in a given string `s`. The input string `s` can contain any printable ASCII characters. The solution should have a time complexity of O(n), where n is the length of the input string.
"""

def length_of_longest_substring(s):
    last_seen = {}
    start = 0
    max_length = 0

    for end, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length