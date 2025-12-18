"""
QUESTION:
Create a function `identify_palindromes(str_1, str_2)` that takes two strings as input and returns the palindromic strings. The function should ignore special characters, punctuation, and capitalization when checking for palindromes. If both strings are palindromes, return both; if only one is a palindrome, return that one; otherwise, return an error message indicating that neither string is a palindrome.
"""

def identify_palindromes(str_1, str_2):
    # Convert strings to lower case, remove spaces and special characters/punctuation
    string1 = ''.join(c for c in str_1 if c.isalnum()).lower()
    string2 = ''.join(c for c in str_2 if c.isalnum()).lower()

    # Reverse the strings
    reverse_string1 = string1[::-1]
    reverse_string2 = string2[::-1]

    # Check if strings are palindromes
    string1_is_palindrome = string1 == reverse_string1
    string2_is_palindrome = string2 == reverse_string2

    if string1_is_palindrome and string2_is_palindrome:
        return str_1, str_2
    elif string1_is_palindrome:
        return str_1
    elif string2_is_palindrome:
        return str_2
    else:
        return "None of the strings is a palindrome"