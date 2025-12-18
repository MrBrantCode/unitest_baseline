"""
QUESTION:
Find the longest substring of unique characters in a given string without using any built-in string functions or data structures. The solution should have a time complexity of O(n). The function, named `find_longest_substring`, should take one argument `string` which can contain any ASCII characters and return or print the longest substring of unique characters along with its starting and ending indices.
"""

def find_longest_substring(string):
    start = 0
    max_length = 0
    seen = {}
    max_start = 0
    
    for i, char in enumerate(string):
        if char in seen and start <= seen[char]:
            start = seen[char] + 1
        
        seen[char] = i
        length = i - start + 1
        
        if length > max_length:
            max_length = length
            max_start = start
    
    return string[max_start:max_start+max_length], max_start, max_start + max_length - 1