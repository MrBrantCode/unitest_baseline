"""
QUESTION:
Write a Python function named 'concatenateAlphabets' that takes two string parameters, combines them into one string, removes any duplicate characters while preserving their original order, and returns only the alphabetical characters in lowercase. The input strings may contain special characters and numbers, which should be ignored in the final output.
"""

from collections import OrderedDict

def concatenateAlphabets(str1, str2):
    # concatenating both the strings
    str3 = str1 + str2
    # removing the duplicate characters using OrderedDict
    str3 = "".join(OrderedDict.fromkeys(str3))
    # initializing an empty string
    result = ''
    # traversing through the string and keeping only alphabets
    for char in str3:
        if char.isalpha():
            result += char.lower()
    return result