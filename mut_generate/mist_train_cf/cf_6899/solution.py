"""
QUESTION:
Create a function named `is_anagram` that takes two strings as parameters and returns True if they are anagrams of each other and False otherwise. The function should be case-sensitive, ignore any spaces in the strings, and handle special characters by excluding them from the comparison. The input strings may contain alphanumeric characters, spaces, and special characters.
"""

def is_anagram(string1, string2):
    # Remove spaces from the strings
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    # Remove special characters from the strings
    string1 = ''.join(e for e in string1 if e.isalnum())
    string2 = ''.join(e for e in string2 if e.isalnum())

    # Check if the sorted strings are equal
    return sorted(string1) == sorted(string2)