"""
QUESTION:
Create a function `longest_substring_length` to find the length of the longest substring without duplicate characters in a given string. The function should only accept strings containing alphabetic characters and return an error message if the input string contains non-alphabetic characters.
"""

def longest_substring_length(s):
    if not s.isalpha():
        return "Error: Input string contains non-alphabetic characters."
    
    max_length = 0
    start = 0
    visited = {}
    
    for i in range(len(s)):
        if s[i] in visited and start <= visited[s[i]]:
            start = visited[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        
        visited[s[i]] = i
    
    return max_length