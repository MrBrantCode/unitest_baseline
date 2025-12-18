"""
QUESTION:
Write a Python function named `common_letters` that takes two strings as input, `str1` and `str2`, and returns a dictionary where the keys are the common letters between the two strings and the values are the frequencies of each letter. The function should be case-insensitive, ignore non-alphabetic characters, and have a time complexity of O(n), where n is the length of the longer string. Do not use any built-in Python functions or libraries for string manipulation or counting, and do not use any additional data structures such as lists or sets to store intermediate results.
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

    # Initialize an empty dictionary to store the final common letters and their frequencies
    common_frequencies = {}

    # Iterate over each character in the frequencies dictionary
    for char in frequencies:
        # Initialize a counter to store the frequency of the character in the second string
        count = 0
        # Iterate over each character in the second string
        for c in str2:
            # Check if the character is the same as the current character in the frequencies dictionary
            if char == c:
                # Increment the counter
                count += 1
        # Update the frequency of the character in the common_frequencies dictionary
        common_frequencies[char] = min(frequencies[char], count)

    return common_frequencies