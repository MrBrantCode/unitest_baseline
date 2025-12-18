"""
QUESTION:
Write a function named `find_mismatch_index` that compares two strings character by character and returns the index of the first mismatch. The function should return -1 if no mismatch is found. The input strings will have the same length, ranging from 1 to 1000 characters.
"""

def find_mismatch_index(string1, string2):
    # Ensure the strings have the same length
    if len(string1) != len(string2):
        return -1  # Mismatch is not possible
    
    # Iterate through each character of the strings
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return i  # Return the index of the first mismatch
    
    return -1  # No mismatch found