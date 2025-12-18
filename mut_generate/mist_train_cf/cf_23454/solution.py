"""
QUESTION:
Write a function called is_anagram that takes two parameters, str1 and str2. The function should return True if str1 and str2 are anagrams of each other and False otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should be case-insensitive and ignore any differences in case between the input strings.
"""

def is_anagram(str1, str2):
    """
    Checks if two input strings are anagrams of each other.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        bool: True if str1 and str2 are anagrams, False otherwise.
    """
    # Compare the length of the two strings
    if len(str1) != len(str2):
        return False

    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Store the frequency of characters in the first string
    frequency_counter1 = {}
    for char in str1:
        frequency_counter1[char] = frequency_counter1.get(char, 0) + 1

    # Store the frequency of characters in the second string
    frequency_counter2 = {}
    for char in str2:
        frequency_counter2[char] = frequency_counter2.get(char, 0) + 1

    # Compare the frequency of characters
    for key in frequency_counter1:
        if key not in frequency_counter2 or frequency_counter2[key] != frequency_counter1[key]:
            return False

    return True