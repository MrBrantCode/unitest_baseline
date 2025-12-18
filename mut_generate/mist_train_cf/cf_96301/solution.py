"""
QUESTION:
Create a function `sort_and_remove_duplicates` that takes a string containing only lowercase alphabets as input and returns a list of unique characters in ascending order. The function should have a time complexity of O(n log n) and space complexity of O(n), where n is the length of the input string.
"""

def sort_and_remove_duplicates(string):
    result = []
    seen = {}
    
    for c in string:
        if c not in seen:
            result.append(c)
            seen[c] = True
    
    return sorted(result)