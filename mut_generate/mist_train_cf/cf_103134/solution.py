"""
QUESTION:
Write a function named `check_anagram` that takes two input strings as parameters. The function should check if the second string is an anagram of the first one, handling strings containing special characters and spaces, and being case-sensitive. The function should return a boolean value indicating whether the second string is an anagram of the first one.
"""

def check_anagram(string1, string2):
    # Remove special characters and spaces
    string1 = ''.join(e for e in string1 if e.isalnum())
    string2 = ''.join(e for e in string2 if e.isalnum())

    # Check if the lengths of both strings are equal
    if len(string1) != len(string2):
        return False

    # Count the occurrence of each character in both strings
    count1 = [0] * 256
    count2 = [0] * 256

    for i in range(len(string1)):
        count1[ord(string1[i])] += 1
        count2[ord(string2[i])] += 1

    # Check if the count of characters in both strings is equal
    for i in range(256):
        if count1[i] != count2[i]:
            return False

    return True