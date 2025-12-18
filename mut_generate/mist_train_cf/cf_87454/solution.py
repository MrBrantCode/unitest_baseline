"""
QUESTION:
Write a Python function `common_letters(str1, str2)` that finds the common letters between two strings, ignoring case, spaces, and special characters, and returns a dictionary where the keys are the common letters and the values are their frequencies in both strings. Implement this function manually without using built-in string manipulation or counting functions, and without using additional data structures like lists or sets. The function should have a time complexity of O(n), where n is the length of the longer string.
"""

def common_letters(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Initialize an empty dictionary to store the frequencies of common letters
    frequencies = {}

    # Iterate over each character in the first string
    for char in str1:
        # Check if the character is a letter and is present in the second string
        if char.isalpha() and char in str2:
            # Check if the character is already in the frequencies dictionary
            if char in frequencies:
                # Increment the frequency of the character
                frequencies[char] += 1
            else:
                # Add the character to the frequencies dictionary with a frequency of 1
                frequencies[char] = 1

    return frequencies