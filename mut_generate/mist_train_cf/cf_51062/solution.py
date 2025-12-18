"""
QUESTION:
Write a function `palindrome_counter` that takes a string as input and returns a boolean indicating whether the input string is a palindrome (ignoring non-alphanumeric characters and case sensitivities) and an integer representing the number of pairs of the same characters that read the same forwards and backwards.
"""

def palindrome_counter(input_string):
    # Make the string lower case and strip all non-alphanumeric characters
    normalized_string = ''.join(e.lower() for e in input_string if e.isalnum())
    
    # Check if the string is a palindrome
    is_palindrome = normalized_string == normalized_string[::-1]

    # Initialize counter for character pairs
    char_pair_counter = 0

    # Create counter of character frequencies in the string 
    from collections import Counter
    freq_counter = Counter(normalized_string)

    # Check for character pairs
    for key in freq_counter:
        char_pair_counter += freq_counter[key] // 2
    
    return is_palindrome, char_pair_counter