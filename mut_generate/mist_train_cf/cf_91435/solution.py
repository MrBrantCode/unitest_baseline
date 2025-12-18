"""
QUESTION:
Write a function `smallest_window(string1, string2)` that takes two strings as input and returns the smallest substring of `string1` containing all characters of `string2`. If no such window is found, return an empty string.
"""

def smallest_window(string1, string2):
    chars_to_find = set(string2)
    char_count = {}
    start = 0
    end = 0
    min_length = float('inf')
    min_start = -1
    found_chars = 0

    while end < len(string1):
        char = string1[end]
        char_count[char] = char_count.get(char, 0) + 1
        
        if char in chars_to_find and char_count[char] == string2.count(char):
            found_chars += 1
        
        while found_chars == len(chars_to_find):
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start
            
            char = string1[start]
            char_count[char] -= 1
            
            if char in chars_to_find and char_count[char] < string2.count(char):
                found_chars -= 1
            
            start += 1
        
        end += 1
    
    if min_start == -1:
        return ""
    
    return string1[min_start:min_start + min_length]