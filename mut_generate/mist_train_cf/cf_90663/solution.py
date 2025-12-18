"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that determines if two strings are anagrams of each other with a time complexity of O(n) and constant space usage, where n is the length of the strings. The function should return `True` if the strings are anagrams, and `False` otherwise.
"""

def are_anagrams(str1, str2):
    # If lengths of strings are not equal, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Initialize a variable for counting purposes
    count = 0
    
    # Iterate through each character in the first string
    for i in range(len(str1)):
        # Convert the characters to ASCII values and XOR them
        count ^= ord(str1[i])
        # Convert the characters of the second string to ASCII values and XOR them
        count ^= ord(str2[i])
    
    # If the count is zero, both strings are anagrams
    return count == 0