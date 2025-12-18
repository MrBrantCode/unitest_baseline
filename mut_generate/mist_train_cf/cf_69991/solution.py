"""
QUESTION:
Design a function `remove_repeats(input_string, case_sensitive=True)` that takes a string and a boolean flag indicating case sensitivity, removes consecutive repeating characters from the string, and returns a tuple containing the resulting string and a dictionary with the count of removed characters for each character type. The function should handle both case sensitive and case insensitive modes.
"""

def remove_repeats(input_string, case_sensitive=True):
    # If not case sensitive, convert string to lower-case
    if not case_sensitive:
        input_string = input_string.lower()

    last_char = ""
    counts = {}
    new_string = ""

    # Iterate over each character in the input string
    for char in input_string:
        # If this character is not the same as the last one, add it to new_string
        if char != last_char:
            new_string += char
            last_char = char
        # Update the count for this character
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return new_string, counts