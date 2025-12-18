"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that checks if two strings are anagrams. The function should not use any built-in sorting or hashing functions or libraries and should not use any auxiliary data structures. The strings only contain lowercase alphabets. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def are_anagrams(str1, str2):
    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False

    # Initialize frequency arrays for each character
    char_freq = [0] * 26

    # Count the frequency of each character in str1
    for char in str1:
        char_freq[ord(char) - ord('a')] += 1

    # Decrease the frequency of each character in str2
    for char in str2:
        char_freq[ord(char) - ord('a')] -= 1

    # Check if any character frequency is non-zero
    for freq in char_freq:
        if freq != 0:
            return False

    return True