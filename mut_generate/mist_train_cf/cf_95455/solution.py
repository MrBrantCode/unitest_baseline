"""
QUESTION:
Create a function `find_longest_string` that takes a list of strings as input and returns the longest string in the list. If multiple strings have the same maximum length, return the first occurrence. If the input list is empty, return `None`. The function should handle strings with leading and trailing whitespaces by removing them before comparison. The input list will contain at most 100 strings and each string will have at most 50 characters.
"""

def find_longest_string(input_list):
    if not input_list:  # check if input list is empty
        return None
    
    longest_string = input_list[0].strip()  # remove leading/trailing whitespaces
    max_length = len(longest_string)
    
    for string in input_list[1:]:
        string = string.strip()  # remove leading/trailing whitespaces
        length = len(string)
        if length > max_length:
            longest_string = string
            max_length = length
    
    return longest_string