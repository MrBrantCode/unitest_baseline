"""
QUESTION:
Implement a function `extractCustomStrings(input_string)` that takes a string `input_string` (1 <= len(input_string) <= 1000) as input. The function should extract all substrings that start with "!@[" and end with "]" from the input string, concatenate them together in the order they appear, and return the resulting string. If no such substrings are found, return an empty string.
"""

def extractCustomStrings(input_string):
    result = ""
    start_sequence = "!@["
    end_sequence = "]"
    start_index = input_string.find(start_sequence)
    
    while start_index != -1:
        end_index = input_string.find(end_sequence, start_index + len(start_sequence))
        if end_index != -1:
            result += input_string[start_index + len(start_sequence):end_index]
            start_index = input_string.find(start_sequence, end_index + len(end_sequence))
        else:
            break
    
    return result