"""
QUESTION:
Write a recursive function called "lastIndexOf" that takes in two parameters: a string "str" and a character "char". The function should return the index of the LAST occurrence of "char" within "str", considering both uppercase and lowercase characters as the same. If "char" is not found, the function should return -1.
"""

def lastIndexOf(str, char):
    if len(str) == 0:
        return -1
    elif str[-1].lower() == char.lower():
        return len(str) - 1
    else:
        return lastIndexOf(str[:-1], char)