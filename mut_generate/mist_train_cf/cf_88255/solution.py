"""
QUESTION:
Write a function named are_anagrams that takes two strings as input and returns True if the strings are anagrams of each other and False otherwise. The function should be case insensitive, consider non-English characters and special characters as valid, and handle multiple occurrences of the same character. It should optimize the algorithm to have a time complexity of O(n) or less, use only constant extra space, and not use any built-in sorting functions or libraries.
"""

def are_anagrams(str1, str2):
    # Initialize frequency counts for each character
    freq1 = [0] * 256
    freq2 = [0] * 256

    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Update the frequency counts for each character in str1
    for char in str1:
        freq1[ord(char)] += 1

    # Update the frequency counts for each character in str2
    for char in str2:
        freq2[ord(char)] += 1

    # Compare the frequency counts
    for i in range(256):
        if freq1[i] != freq2[i]:
            return False

    return True