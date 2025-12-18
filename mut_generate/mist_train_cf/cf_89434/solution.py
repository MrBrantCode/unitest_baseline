"""
QUESTION:
Create a function named `is_anagram` that takes two strings as input, and returns a boolean indicating whether they are anagrams. The function must be case-insensitive, have a time complexity of O(n) where n is the length of the longer string, have a space complexity of O(1), and not use built-in functions or methods for comparing characters or sorting the strings. It should also handle strings with Unicode characters.
"""

def is_anagram(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Initialize a dictionary to store the character frequencies
    char_freq = {}

    # Count the frequency of characters in str1
    for char in str1:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Subtract the frequency of characters in str2
    for char in str2:
        if char in char_freq:
            char_freq[char] -= 1
        else:
            char_freq[char] = -1

    # Check if all character frequencies are 0
    for freq in char_freq.values():
        if freq != 0:
            return False

    return True