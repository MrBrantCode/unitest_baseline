"""
QUESTION:
Write a recursive function named `count_lowercase` that takes a string as input and returns the count of lowercase alphabets excluding the letter 'a'.
"""

def count_lowercase(str):
    if len(str) == 0:  # base case: empty string
        return 0
    elif str[0] == 'a':  # excluding 'a'
        return count_lowercase(str[1:])
    elif str[0].islower():  # lowercase alphabets
        return 1 + count_lowercase(str[1:])
    else:  # non-lowercase alphabets
        return count_lowercase(str[1:])