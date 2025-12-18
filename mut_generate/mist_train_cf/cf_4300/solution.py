"""
QUESTION:
Write a function `compare_strings(string1, string2)` that compares two strings character by character and returns the number of matching alphabetic characters. The function should only consider alphabetic characters (both lowercase and uppercase) and ignore any non-alphabetic characters. If the input strings are not of equal length, the function should return an error message.
"""

import re

def compare_strings(string1, string2):
    # Check if the input strings are of equal length
    if len(string1) != len(string2):
        return "Error: The lengths of the strings are not equal"
    
    # Initialize a counter to store the number of matching characters
    count = 0
    
    # Iterate through the characters in the strings
    for i in range(len(string1)):
        # Check if the current characters in both strings are alphabetic
        if re.match("^[a-zA-Z]+$", string1[i]) and re.match("^[a-zA-Z]+$", string2[i]):
            # If the alphabetic characters match, increment the counter
            if string1[i] == string2[i]:
                count += 1
    
    # Return the count of matching alphabetic characters
    return count