"""
QUESTION:
Write a function `remove_repeats(s)` that takes a string `s` as input, removes repeated characters, and returns the resulting string along with a dictionary that stores the frequency of each character in the original string. The function should allow for efficient lookups of character frequencies. The function must return two values: the string with no repeated characters and a dictionary of character frequencies.
"""

def remove_repeats(s):
    # Initialize an empty string to hold the final result
    final_str = ""

    # Initialize an empty dictionary to hold character counts
    char_counts = {}

    # Initialize a variable to hold the last seen character
    last_char = None

    # Iterate over each character in the string
    for char in s:
        # If the character is the same as the last seen character, increment the count
        if char == last_char:
            char_counts[char] += 1
        else:
            # Else, add the character to the final string and set its count to 1
            final_str += char
            char_counts[char] = char_counts.get(char, 0) + 1

        # Update the last seen character
        last_char = char

    return final_str, char_counts