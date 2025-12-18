"""
QUESTION:
Write a function `remove_and_count_chars` that takes a string as input and returns a tuple containing the modified string with all occurrences of 'a', 'b', and 'c' removed, and the counts of 'a', 'b', and 'c' in the original string. Assume the input string contains at least 5 occurrences of each of the characters 'a', 'b', and 'c'.
"""

def remove_and_count_chars(input_string):
    # Initialize count variables
    count_a = 0
    count_b = 0
    count_c = 0
    
    # Remove characters 'a', 'b', and 'c' from the string
    modified_string = input_string.replace('a', '').replace('b', '').replace('c', '')
    
    # Count the occurrences of characters 'a', 'b', and 'c' in the original string
    for char in input_string:
        if char == 'a':
            count_a += 1
        elif char == 'b':
            count_b += 1
        elif char == 'c':
            count_c += 1
    
    return modified_string, count_a, count_b, count_c