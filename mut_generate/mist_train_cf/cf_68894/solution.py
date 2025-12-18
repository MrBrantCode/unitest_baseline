"""
QUESTION:
Write a function `longest_substring` that takes an input string and returns the lengthiest substring consisting of the same character. The function should use an iterative approach and handle unicode characters. The input string can be empty or contain any combination of ASCII and unicode characters.
"""

def longest_substring(input_string):
    if not input_string: 
        return ''
        
    max_length = curr_length = 1
    max_str = curr_str = input_string[0]

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            curr_length += 1
            curr_str += input_string[i]
        else:
            curr_length = 1
            curr_str = input_string[i]

        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

    return max_str