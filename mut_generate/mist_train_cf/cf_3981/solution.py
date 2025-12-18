"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that determines if two strings are anagrams of each other. The function should consider the following constraints and requirements: the comparison should be case insensitive, handle strings of different lengths and different character types, handle special characters, and multiple occurrences of the same character in both strings. The function should optimize the algorithm to have a time complexity of O(n) or less, use only constant extra space, and handle large inputs efficiently with a maximum combined length of 10^6 characters. The function should output the result of whether the strings are anagrams, and should be implemented without using any built-in sorting functions or libraries, and using a single loop for comparing the characters in both strings is not required but preferred.
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