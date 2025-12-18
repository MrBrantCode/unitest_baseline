"""
QUESTION:
Implement a function named `count_differences` that takes two binary strings `str1` and `str2` as input and returns the number of differences between them. The function should assume that the length of the two input strings can be up to 10^7 characters. The function must not use any string comparison or built-in functions for comparing characters. If the input strings have different lengths, the function should return -1.
"""

def count_differences(str1, str2):
    # Get the length of the input strings
    len1 = len(str1)
    len2 = len(str2)

    # If the lengths are not equal, return -1
    if len1 != len2:
        return -1

    # Initialize the counter for differences
    count = 0

    # Iterate through both strings simultaneously
    for i in range(len1):
        # Get the characters at the current index
        char1 = str1[i]
        char2 = str2[i]

        # Check if the characters are different
        if char1 != char2:
            count += 1

    # Return the number of differences
    return count