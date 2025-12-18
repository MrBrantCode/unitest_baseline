"""
QUESTION:
Write a function named `are_anagrams` that determines whether two input strings are anagrams of each other without using built-in functions or libraries for sorting or counting characters. The function should have a time complexity of O(n), where n is the length of the input strings, and should not use additional data structures such as dictionaries or lists beyond what is necessary to solve the problem. The function should ignore spaces in the input strings.
"""

def are_anagrams(str1, str2):
    # Remove spaces from the strings
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')

    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False

    # Initialize an empty list to keep track of characters
    characters = [0] * 26

    # Count the occurrences of each character in str1
    for char in str1:
        index = ord(char.lower()) - ord('a')
        characters[index] += 1

    # Subtract the occurrences of each character in str2
    for char in str2:
        index = ord(char.lower()) - ord('a')
        characters[index] -= 1

    # Check if there are any non-zero counts
    for count in characters:
        if count != 0:
            return False

    # All counts are zero, so the strings are anagrams
    return True