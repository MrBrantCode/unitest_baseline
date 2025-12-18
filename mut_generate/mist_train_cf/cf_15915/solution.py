"""
QUESTION:
Write a function `find_most_frequent_character` that takes a string as input and returns the most frequent character in the string, considering both uppercase and lowercase characters as the same. The function should have a time complexity of O(n), where n is the length of the input string, and should be able to handle strings with up to 1,000,000 characters.
"""

def find_most_frequent_character(string):
    # Dictionary to store frequency count of characters
    frequency = {}

    # Iterate through each character in the string
    for char in string:
        # Convert character to lowercase
        char = char.lower()

        # Update frequency count in the dictionary
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find the character with maximum frequency
    max_freq = 0
    most_frequent_char = ''
    for char, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_char = char

    return most_frequent_char