"""
QUESTION:
Create a function `count_binary_string_differences` that compares two binary strings `str1` and `str2` and returns the number of differences between them. The function should return -1 if the lengths of the two input strings are different. The function should be able to handle strings of up to 10^6 characters in length.
"""

def count_binary_string_differences(str1, str2):
    # Check if the lengths of the two strings are different
    if len(str1) != len(str2):
        return -1  # Return -1 to indicate different lengths
    
    count = 0  # Initialize the count of differences to 0
    
    # Iterate over each character in the strings
    for i in range(len(str1)):
        # If the characters at the current index are different, increment the count
        if str1[i] != str2[i]:
            count += 1
    
    return count