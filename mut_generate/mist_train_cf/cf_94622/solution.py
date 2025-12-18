"""
QUESTION:
Create a function named `reverse_and_remove_duplicates` that takes a string as input. The function should return a new string that is the reversed version of the original string with no duplicate characters, where each character is followed by its count in the original string.
"""

def reverse_and_remove_duplicates(input_string):
    # Reverse the input string
    reversed_string = input_string[::-1]

    # Remove duplicate characters
    unique_chars = []
    for char in reversed_string:
        if char not in unique_chars:
            unique_chars.append(char)

    # Count occurrences of each character in the original string
    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Create the final output string
    final_string = ''
    for char in unique_chars:
        final_string += char + str(char_counts[char])

    return final_string