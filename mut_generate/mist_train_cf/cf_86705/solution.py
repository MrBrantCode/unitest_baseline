"""
QUESTION:
Write a function `find_substring_index(string, substring)` that finds the first index of `substring` in `string`. The function should have a time complexity of O(n), where n is the length of `string`, and a space complexity of O(1). The function should be case-insensitive and should not use any built-in string search functions or regular expressions. If `substring` is not found in `string`, the function should return -1.
"""

def find_substring_index(string, substring):
    string = string.lower()
    substring = substring.lower()
    
    start = 0
    end = len(substring)
    
    while end <= len(string):
        if string[start:end] == substring:
            return start
        
        start += 1
        end += 1
    
    return -1