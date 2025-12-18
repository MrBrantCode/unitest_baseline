"""
QUESTION:
Write a function `find_most_common_char` that takes a string containing only alphabetic characters and spaces as input, and prints the most frequently occurring character(s) in alphabetical order. If there are multiple characters with the same maximum frequency, print all of them. If the input string is empty or contains only spaces, print "No characters found." The function should ignore case and leading/trailing spaces.
"""

def find_most_common_char(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Convert the string to lowercase
    string = string.lower()

    # Create a dictionary to store the frequency of each character
    char_freq = {}

    # Iterate over each character in the string
    for char in string:
        # Ignore spaces
        if char != ' ':
            # Increment the frequency count of the character
            char_freq[char] = char_freq.get(char, 0) + 1

    # If no characters found, print the appropriate message
    if not char_freq:
        print("No characters found.")
        return

    # Find the maximum frequency among the characters
    max_freq = max(char_freq.values())

    # Create a list to store the most commonly-used characters
    most_common_chars = []

    # Iterate over the characters and their frequencies
    for char, freq in char_freq.items():
        # If the frequency is equal to the maximum frequency, add the character to the list
        if freq == max_freq:
            most_common_chars.append(char)

    # Sort the most_common_chars list in alphabetical order
    most_common_chars.sort()

    # Print the most commonly-used characters
    print("Most commonly-used character(s):", ", ".join(most_common_chars))