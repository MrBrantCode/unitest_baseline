"""
QUESTION:
Create a function named `count_binary_string_differences` that compares two binary strings of up to 10^6 characters and returns the number of differences between them. If the lengths of the two input strings are different, return -1.
"""

def entrance(str1, str2):
    if len(str1) != len(str2):
        return -1
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count