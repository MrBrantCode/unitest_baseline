"""
QUESTION:
Create a function named `common_characters` that takes two input strings `str1` and `str2`. The function should return a string containing unique characters that are common to both `str1` and `str2`, excluding any character that appears more times than the length of the shorter string. The returned string should be sorted in ascending order. The function should not use any built-in Python string functions or modules for sorting and removing duplicates. Provide example inputs and expected outputs to demonstrate the function's behavior.
"""

def common_characters(str1: str, str2: str) -> str:
    # Create a dictionary for each string
    dict1 = {}
    dict2 = {}
    strOut = ""
    # Count number of occurrences of each character
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    for char in str2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1

    # Find intersection
    for key in dict1:
        if key in dict2 and dict1[key] <= len(str2) and dict2[key] <= len(str1):
            strOut += key

    # Sort the string without using in-built function
    for i in range(len(strOut)):
        for j in range(i + 1, len(strOut)):
            if strOut[i] > strOut[j]:
                strOut = strOut[:i] + strOut[j] + strOut[i+1:j] + strOut[i] + strOut[j+1:]

    return strOut