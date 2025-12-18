"""
QUESTION:
Create two functions, `is_palindrome` and `make_palindrome`, that ignore case and non-alphanumeric characters. The `is_palindrome` function should return a boolean indicating whether the input string is a palindrome. The `make_palindrome` function should generate the minimal-length palindrome having the initial string as the prefix. The algorithm for `make_palindrome` involves finding the longest palindrome postfix within the given string, reversing the string prefix preceding the palindromic suffix, and attaching it at the end of the original string. Do not import any extra modules or libraries.
"""

def entrance(string: str) -> str:
    cleaned_string = ''.join(filter(str.isalnum, string)).lower()
    palindromic_suffix = ""
    for index in range(len(cleaned_string)):
        temp = cleaned_string[index:]
        if temp == temp[::-1]:
            palindromic_suffix = temp
            break

    non_palindromic_prefix = cleaned_string[:-len(palindromic_suffix)] if palindromic_suffix else cleaned_string
    result = string + non_palindromic_prefix[::-1]

    return result