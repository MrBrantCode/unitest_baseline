"""
QUESTION:
Create a function named `check_strings` that takes two string parameters. The function should return "Palindrome" if the strings are of equal length, contain only lowercase alphabetic characters, and the first string is the same forwards and backwards. Return "Not Palindrome" if the strings meet the length and character requirements but the first string is not a palindrome. Otherwise, return False.
"""

def check_strings(str1, str2):
    if len(str1) == len(str2) and str1.islower() and str2.islower():
        if str1 == str1[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome"
    else:
        return False