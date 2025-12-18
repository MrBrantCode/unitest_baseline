"""
QUESTION:
Create a function named `find_longest_string` that takes an input list of strings. The function should return the longest string in the list, resolving ties by returning the first occurrence. If the input list is empty, return `None`. The function must handle strings with leading and trailing whitespaces.
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