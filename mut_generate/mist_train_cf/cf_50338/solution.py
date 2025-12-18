"""
QUESTION:
Write a function `longest_palindrome` that finds the longest palindromic substring in a given string. The function should take a string as input and return the longest substring that reads the same forward and backward.
"""

def longest_palindrome(textual_fragment):
    res = ""
    for i in range(len(textual_fragment)):
        for j in range(len(textual_fragment), i, -1): 
            if len(res) >= j-i: 
                break
            elif textual_fragment[i:j] == textual_fragment[i:j][::-1]: 
                res = textual_fragment[i:j]
    return res