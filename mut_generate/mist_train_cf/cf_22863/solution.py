"""
QUESTION:
Create a function separate_string that takes a string of alphanumeric characters as input. The function should separate the string into two parts, with the left part containing only digits in non-decreasing order and the right part containing only lowercase letters. If there are no lowercase letters, the right part should be an empty string. The time complexity of the solution should be O(n log n), where n is the length of the string.
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