"""
QUESTION:
Write a function `longest_substring(s)` that finds the longest substring with non-repeating characters in a given string `s`. The function should handle empty strings, single character strings, special characters, and whitespace, and it should have a time complexity of O(n), where n is the length of the string. Do not use any built-in functions or libraries that directly solve this problem.
"""

def longest_substring(s):
    if len(s) <= 1:
        return s
    
    start = 0
    max_len = 0
    visited = {}
    
    for i in range(len(s)):
        if s[i] in visited and start <= visited[s[i]]:
            start = visited[s[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        
        visited[s[i]] = i
    
    return s[start:start+max_len]