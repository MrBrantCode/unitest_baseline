"""
QUESTION:
Write a function named `are_anagrams` that checks if two input strings are anagrams, ignoring case and whitespace differences, without using built-in sorting or hashing functions or libraries. The function should return `True` if the strings are anagrams and `False` otherwise. Assume the input strings only contain English alphabet letters.
"""

def are_anagrams(str1, str2):
    # Convert strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Create arrays to store counts of each letter
    count1 = [0] * 26
    count2 = [0] * 26

    # Update counts for each letter in the first string
    for char in str1:
        index = ord(char) - ord('a')
        count1[index] += 1

    # Update counts for each letter in the second string
    for char in str2:
        index = ord(char) - ord('a')
        count2[index] += 1

    # Check if the counts are equal in both arrays
    for i in range(26):
        if count1[i] != count2[i]:
            return False

    return True