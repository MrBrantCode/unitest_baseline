"""
QUESTION:
Write a function `reverse_substring(string, n)` that takes a string and an integer `n` as input and returns the modified string where the substring starting from the `n`th character and ending at the `(2*n)`th character is reversed. If there are less than `(2*n)` characters after the `n`th character, reverse the substring until the end of the string. The input string will contain only lowercase alphabets and the value of `n` will be a positive integer.
"""

def entance(string, n):
    if len(string) <= n:
        return string

    if len(string) <= 2 * n:
        return string[:n] + string[n:][::-1]

    return string[:n] + string[n:2 * n][::-1] + string[2 * n:]