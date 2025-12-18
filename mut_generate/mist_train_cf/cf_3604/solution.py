"""
QUESTION:
Write a function `is_anagram` that determines if two input strings are anagrams of each other. The function should be case-insensitive, handle special characters and spaces, and have a time complexity of O(n) and space complexity of O(1), where n is the length of the strings. The function should not use any built-in sorting functions or libraries, and should not use additional data structures to store the character frequencies.
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