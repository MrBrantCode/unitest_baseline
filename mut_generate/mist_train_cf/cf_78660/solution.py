"""
QUESTION:
Create a function named `sort_strings` that takes a list of strings as input, where each string contains an integer between 1 and 99. The function should sort the list alphabetically and then by the integer value in ascending order. The output should be a sorted list of strings.
"""

import functools

# Function to extract the number from the string
def extract_number(s):
    return int(''.join(filter(str.isdigit, s)))

# Function to extract the string part from the string
def extract_string(s): 
    return ''.join(filter(str.isalpha, s))

# Custom comparator
def compare_items(a, b):
    # Extract string and number part
    a_string_part = extract_string(a)
    b_string_part = extract_string(b)
    a_number_part = extract_number(a)
    b_number_part = extract_number(b)
    
    # Comparison based on the string part and the number part
    if a_string_part < b_string_part:
        return -1
    elif a_string_part > b_string_part:
        return 1
    else:
        if a_number_part < b_number_part:
            return -1
        elif a_number_part  > b_number_part:
            return 1
        else:
            return 0

# Main function
def sort_strings(lst):
    return sorted(lst, key=functools.cmp_to_key(compare_items))