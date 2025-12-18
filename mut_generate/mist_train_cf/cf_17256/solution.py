"""
QUESTION:
Create a function named `reverse_and_remove_duplicates` that takes a string `input_string` as input and returns a new string. The function should reverse the input string, remove any duplicate characters from the reversed string, and include the count of each character from the original string in the final output.
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