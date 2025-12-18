"""
QUESTION:
Create a function `remove_and_count_chars` that takes a string `input_string` as input. The function should remove all occurrences of 'a', 'b', and 'c' from `input_string` and return a dictionary with the count of each removed character. The input string may contain leading or trailing whitespace, which should be ignored.
"""

def remove_and_count_chars(input_string):
    # Remove leading and trailing whitespace
    input_string = input_string.strip()

    # Initialize dictionary to store counts
    counts = {'a': 0, 'b': 0, 'c': 0}

    # Remove 'a', 'b', and 'c' from the string and update the counts
    for char in input_string:
        if char in ['a', 'b', 'c']:
            input_string = input_string.replace(char, '', 1)
            counts[char] += 1

    return counts