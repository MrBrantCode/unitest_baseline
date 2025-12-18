"""
QUESTION:
Create a function `string_difference(str1, str2)` that takes two text strings as input and returns the number of characters that are different between the two strings, excluding spaces. The function should be case-sensitive and consider characters with different case as different. The input strings can be of any length and may contain special characters, but it is assumed that both strings have the same length after removing spaces.
"""

def string_difference(str1, str2):
    # Remove spaces from both strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Initialize the difference count
    difference = 0

    # Iterate through each character in the strings
    for i in range(len(str1)):
        # Check if the characters at the current index are different
        if str1[i] != str2[i]:
            difference += 1

    return difference