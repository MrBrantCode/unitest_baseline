"""
QUESTION:
Write a function `is_anagram(str1, str2)` that determines if two input strings are anagrams, ignoring case. The function should have a time complexity of O(n), where n is the length of the longer string, and a space complexity of O(1). The function should not use built-in functions or methods to compare characters or sort the strings and should be able to handle strings with Unicode characters.
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