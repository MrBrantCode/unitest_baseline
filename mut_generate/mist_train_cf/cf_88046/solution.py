"""
QUESTION:
Write a function named `is_anagram` that determines if two input strings are anagrams or not, considering only alphanumeric characters, ignoring case and spaces, and without using built-in sorting functions or libraries, with a time complexity of O(n) and constant space complexity. The function should be able to handle strings of length up to 10^6.
"""

def is_anagram(string1, string2):
    # Convert the strings to lowercase and remove special characters and spaces
    string1 = ''.join(c.lower() for c in string1 if c.isalpha())
    string2 = ''.join(c.lower() for c in string2 if c.isalpha())

    # If the lengths of the strings are different, they cannot be anagrams
    if len(string1) != len(string2):
        return False

    # Initialize a list to store the character frequencies
    frequencies = [0] * 26

    # Calculate the character frequencies for string1
    for char in string1:
        frequencies[ord(char) - ord('a')] += 1

    # Subtract the character frequencies for string2
    for char in string2:
        frequencies[ord(char) - ord('a')] -= 1

    # Check if all character frequencies are zero
    for freq in frequencies:
        if freq != 0:
            return False

    return True