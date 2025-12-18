"""
QUESTION:
Write a function called `find_common_letters` that takes two strings `str1` and `str2` as input and returns a dictionary where the keys are the common letters between the two strings and the values are the frequencies of each letter. Both strings are case-insensitive and can contain spaces and special characters. The function must manually implement string manipulation and counting without using any built-in Python functions or libraries. The dictionary should contain each common letter only once with its total frequency in both strings.
"""

def find_common_letters(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Initialize an empty dictionary to store the common letters and their frequencies
    common_letters = {}

    # Iterate over each character in the first string
    for char in str1:
        # Check if the character is a letter and if it is present in the second string
        if char.isalpha() and char in str2:
            # If the character is already in the dictionary, increment its frequency
            if char in common_letters:
                common_letters[char] += 1
            # If the character is not in the dictionary, add it with a frequency of 1
            else:
                common_letters[char] = 1

    # Iterate over each character in the second string
    for char in str2:
        # Check if the character is a letter and if it is present in the first string
        if char.isalpha() and char in str1:
            # If the character is already in the dictionary, increment its frequency
            if char in common_letters:
                common_letters[char] += 1
            # If the character is not in the dictionary, add it with a frequency of 1
            else:
                common_letters[char] = 1

    # Return the dictionary of common letters and their frequencies
    return common_letters