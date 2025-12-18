"""
QUESTION:
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index `0` will be considered even.

For example, `capitalize("abcdef") = ['AbCdEf', 'aBcDeF']`. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try: 

[Indexed capitalization](https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1)

[Even-odd disparity](https://www.codewars.com/kata/59c62f1bdcc40560a2000060)
"""

def capitalize_alternating_indexes(s: str) -> list:
    """
    Capitalizes the letters that occupy even indexes and odd indexes separately in the given string.

    :param s: A lowercase string with no spaces.
    :return: A list containing two strings:
             - The first string has letters at even indexes capitalized.
             - The second string has letters at odd indexes capitalized.
    """
    even_capitalized = ''.join((c if i % 2 else c.upper() for (i, c) in enumerate(s)))
    odd_capitalized = even_capitalized.swapcase()
    return [even_capitalized, odd_capitalized]