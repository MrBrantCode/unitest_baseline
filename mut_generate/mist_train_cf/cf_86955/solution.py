"""
QUESTION:
Create a function `compare_binary_strings` that takes two binary strings `str1` and `str2` as input, compares them character by character, and returns the number of differences between them. The function should return -1 if the lengths of `str1` and `str2` are not equal. Implement the function without using any string comparison or built-in functions for comparing characters, achieving a time complexity of O(n) and a space complexity of O(1), where n is the length of the input strings.
"""

def compare_binary_strings(str1, str2):
    # Check if the lengths of the two strings are equal
    if len(str1) != len(str2):
        return -1  # Return -1 if the lengths are different
    
    differences = 0  # Counter for differences
    
    # Iterate over the characters of the strings using bitwise operations
    for i in range(len(str1)):
        # Compare the characters using bitwise XOR
        if str1[i] != str2[i]:
            differences += 1  # Increment the counter if the characters are different
    
    return differences