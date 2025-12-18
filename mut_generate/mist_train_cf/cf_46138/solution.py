"""
QUESTION:
Write a function called `longest_palindrome` that finds the longest substring of a given string that is a palindrome. The function should return the longest palindrome substring. If no palindrome substring is found, return None.
"""

def longest_palindrome(input_string):
    # reverse input string and compare with original string
    if input_string == input_string[::-1]:
        return input_string

    # get the length of the input string
    str_length = len(input_string)

    # if the original string is not palindrome, start process of checking substrings
    for x in range(str_length, 0, -1):
        for y in range(0, str_length - x + 1):
            substring = input_string[y: y + x]
            # check if the substring is a palindrome
            if substring == substring[::-1]:
                return substring

    # if no palindrome substring found, return none
    return None