"""
QUESTION:
Write a function named `is_anagram` that takes two strings as input and returns a boolean indicating whether the two strings are anagrams of each other. The comparison should be case insensitive, and the function should handle strings containing spaces, punctuation marks, special characters, and multiple occurrences of the same character. The function should also handle strings of different lengths and optimize the algorithm to have a time complexity of O(n) or less.
"""

def is_anagram(s1, s2):
    # Remove spaces and punctuation marks from the strings
    s1 = ''.join(e for e in s1 if e.isalnum())
    s2 = ''.join(e for e in s2 if e.isalnum())
    
    # Convert the strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Create dictionaries to count the occurrences of each character in the strings
    count1 = {}
    count2 = {}
    
    # Count the occurrences of each character in string1
    for char in s1:
        count1[char] = count1.get(char, 0) + 1
    
    # Count the occurrences of each character in string2
    for char in s2:
        count2[char] = count2.get(char, 0) + 1
    
    # Check if the dictionaries are equal
    return count1 == count2