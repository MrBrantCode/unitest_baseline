"""
QUESTION:
Write a function `max_unbroken_sequence` that takes a string `my_string` as input and returns the longest unbroken sequence of identical alphabetical characters in the string. The function should iterate over the string and identify sequences of identical characters, updating the maximum sequence found so far if a longer sequence is encountered.
"""

def max_unbroken_sequence(my_string):
    # Initialize previous character and counts
    prev_char = ''
    max_count = 0
    current_count = 0

    # Initialize sequences
    sequence = ''
    max_sequence = ''

    # Iterate over the string
    for char in my_string:
        # If it's the same as the previous one
        if char == prev_char:
            current_count += 1
            sequence += char
        # If it differs from the previous character, start a new sequence
        else:
            current_count = 1
            sequence = char
        
        # Update maximum if current is larger
        if current_count > max_count:
            max_count = current_count
            max_sequence = sequence
        
        # Update previous character
        prev_char = char

    return max_sequence