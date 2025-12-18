"""
QUESTION:
Write a function `search_occurrences(pattern, text, range_start, range_end)` that takes a pattern string and a text string, and returns a list of unique positions where the pattern occurs in the text, excluding occurrences within the specified range of positions from `range_start` to `range_end`.
"""

def search_occurrences(pattern, text, range_start, range_end):
    occurrences = []
    index = text.find(pattern)
    
    while index != -1:
        if index < range_start or index > range_end:
            occurrences.append(index)
        
        index = text.find(pattern, index + 1)
    
    return occurrences