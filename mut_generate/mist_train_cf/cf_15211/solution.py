"""
QUESTION:
Write a function named `are_anagrams` that takes two strings as input, `str1` and `str2`, and returns `True` if they are anagrams of each other and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the strings, and should use constant space, excluding the input strings. Assume that the input strings only contain lowercase letters and do not use any built-in sorting or hashing functions.
"""

def are_anagrams(str1, str2):
    # If the lengths of the strings are different, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Create a list to store the count of each character in the strings
    count = [0] * 26
    
    # Iterate over each character in the first string
    for i in range(len(str1)):
        # Increment the count of the character at the corresponding index
        # in the count list for the first string
        count[ord(str1[i]) - ord('a')] += 1
        # Decrement the count of the character at the corresponding index
        # in the count list for the second string
        count[ord(str2[i]) - ord('a')] -= 1
    
    # If the counts of the characters in the list are not all zero,
    # the strings are not anagrams
    for i in range(26):
        if count[i] != 0:
            return False
    
    return True