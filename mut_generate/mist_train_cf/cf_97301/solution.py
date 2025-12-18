"""
QUESTION:
Write a function named `separate_string` that takes a string of alphanumeric characters as input, separates it into two parts, and returns the resulting string. The left part should contain only digits in non-decreasing order, and the right part should contain only lowercase letters. If there are no lowercase letters in the string, return an empty string for the right part. The function should have a time complexity of O(n log n), where n is the length of the string.
"""

def separate_string(s):
    leftPart = ""
    rightPart = ""
    
    for char in s:
        if char.isdigit():
            leftPart += char
        elif char.islower():
            rightPart += char
    
    leftPart = ''.join(sorted(leftPart))
    
    if rightPart == "":
        return leftPart
    else:
        return leftPart + rightPart