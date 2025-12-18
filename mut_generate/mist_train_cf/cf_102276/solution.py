"""
QUESTION:
Write a function named `is_anagram` that takes two strings as input and returns True if one string is an anagram of the other, False otherwise. The function should handle strings containing special characters and numbers, ignore whitespace characters, and be case-sensitive, treating uppercase and lowercase letters as distinct characters.
"""

def is_anagram(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    if len(string1) != len(string2):
        return False

    count1 = {}
    count2 = {}

    for char in string1:
        count1[char] = count1.get(char, 0) + 1

    for char in string2:
        count2[char] = count2.get(char, 0) + 1

    return count1 == count2