"""
QUESTION:
Write a function `find_compact_subsequence(input_string)` that finds the shortest subsequence within `input_string` that contains all unique alphabetic characters exactly once. The function should return the shortest subsequence as a string. The input string will only contain alphabetic characters.
"""

def find_compact_subsequence(input_string):
    # dict to save the position of each unique letter
    index_map = {}
    # start and end position of the most compact subsequence
    min_len = float('inf')
    min_start = 0

    # start position of the current subsequence
    start = 0
    for i, char in enumerate(input_string):
        if char in index_map:
            start = max(start, index_map[char] + 1)
        index_map[char] = i
        
        if i - start + 1 < min_len and len(index_map) == len(set(input_string)):
            min_len = i - start + 1
            min_start = start
    
    # return the compact subsequence
    return input_string[min_start:min_start+min_len]