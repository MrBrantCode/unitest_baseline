"""
QUESTION:
Write a function named `is_anagram` that takes two string parameters, `string1` and `string2`, and returns a boolean indicating whether the two strings are anagrams of each other. The function should ignore spaces and punctuation marks, be case insensitive, and handle special characters, multiple occurrences of the same character, and strings of different lengths. The time complexity of the algorithm should be O(n) or less.
"""

def is_anagram(string1, string2):
    # Remove spaces and punctuation marks from the strings
    string1 = ''.join(e for e in string1 if e.isalnum())
    string2 = ''.join(e for e in string2 if e.isalnum())
    
    # Convert the strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()
    
    # Create dictionaries to count the occurrences of each character in the strings
    count1 = {}
    count2 = {}
    
    # Count the occurrences of each character in string1
    for char in string1:
        count1[char] = count1.get(char, 0) + 1
    
    # Count the occurrences of each character in string2
    for char in string2:
        count2[char] = count2.get(char, 0) + 1
    
    # Check if the dictionaries are equal
    return count1 == count2