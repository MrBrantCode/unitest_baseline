"""
QUESTION:
Write a function `longest_substring(input_string)` that finds the longest substring with no repeating characters in the given `input_string`, maintaining the same order of characters as in the input. The function should return this longest substring. The input string can contain any characters and is not guaranteed to be non-empty.
"""

def longest_substring(input_string):
    str_list = []
    longest = 0
    longest_str = ""
    i = 0
    while i < len(input_string):
        if input_string[i] not in str_list:
            str_list.append(input_string[i])
        else:
            if len(str_list) > longest:
                longest = len(str_list)
                longest_str = ''.join(str_list) 
            str_list = [input_string[i]]            
        if i == len(input_string) - 1 and len(str_list) > longest:
            longest = len(str_list)
            longest_str = ''.join(str_list)            
        i += 1
    return longest_str