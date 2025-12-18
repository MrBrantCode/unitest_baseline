"""
QUESTION:
Write a function `shortest_substring(input_string)` that takes an input string and returns the shortest possible substring that contains all the distinct characters in the input string. The time complexity of the function should be O(n), where n is the length of the input string.
"""

def shortest_substring(input_string):
    distinct_chars = set(input_string)
    num_distinct_chars = len(distinct_chars)
    
    char_count = {}
    min_len = float('inf')
    min_substring = ""

    start = 0
    end = 0
    count = 0

    while end < len(input_string):
        char_count[input_string[end]] = char_count.get(input_string[end], 0) + 1
        
        if char_count[input_string[end]] == 1:
            count += 1
        
        while count == num_distinct_chars:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_substring = input_string[start:end+1]
            
            char_count[input_string[start]] -= 1
            
            if char_count[input_string[start]] == 0:
                count -= 1
            
            start += 1
        
        end += 1
    
    return min_substring