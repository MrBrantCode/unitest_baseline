"""
QUESTION:
Write a function `longest_consecutive_substring(string)` that returns the longest substring of consecutive characters in a given string. If there are multiple substrings with the same length, return the one that occurs first.
"""

def longest_consecutive_substring(string):
    if len(string) == 0:
        return ""
    
    longest_substring = string[0]
    current_substring = string[0]
    
    for i in range(1, len(string)):
        if ord(string[i]) - ord(string[i-1]) == 1:
            current_substring += string[i]
        else:
            current_substring = string[i]
        
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
            
    return longest_substring