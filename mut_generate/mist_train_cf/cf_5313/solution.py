"""
QUESTION:
Write a function `longest_substring` that takes a string as input and returns the longest substring without repeating characters. The function should have a time complexity of O(n), where n is the length of the string, and should handle cases where the string is empty or contains only one character, Unicode characters, or special characters. The function should not use any built-in functions or libraries that directly solve this problem.
"""

def longest_substring(s):
    if len(s) <= 1:
        return s

    max_len = 0
    start = 0
    visited = {}
    longest_sub = ""

    for i in range(len(s)):
        if s[i] in visited and start <= visited[s[i]]:
            start = visited[s[i]] + 1
        else:
            if i - start + 1 > max_len:
                max_len = i - start + 1
                longest_sub = s[start:i+1]
        visited[s[i]] = i

    return longest_sub