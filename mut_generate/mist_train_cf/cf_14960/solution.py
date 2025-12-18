"""
QUESTION:
Write a function `compare_strings(str1, str2)` that takes two strings as input and returns the number of character positions at which the strings differ from each other. The function should be case-insensitive, ignore leading and trailing whitespaces, and handle Unicode characters properly.
"""

def compare_strings(str1, str2):
    # Remove leading and trailing whitespaces
    str1 = str1.strip()
    str2 = str2.strip()

    # Convert the strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Initialize a counter for the number of differences
    num_differences = 0

    # Iterate through each character in the strings
    for char1, char2 in zip(str1, str2):
        # Check if the characters are different
        if char1 != char2:
            num_differences += 1

    # Add differences in string lengths
    num_differences += abs(len(str1) - len(str2))

    # Return the number of differences
    return num_differences