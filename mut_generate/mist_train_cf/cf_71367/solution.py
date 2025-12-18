"""
QUESTION:
Write a function `reverse_string_concat(nums)` that takes a list of integers as input, where each integer represents a Unicode code point value. Convert each integer into its corresponding Unicode character, concatenate the characters into a string, and then reverse the string. The function should handle negative integers by shifting them into the positive range without changing their original meaning.
"""

def reverse_string_concat(nums):
    unicode_str = ''.join(chr(n + 65536 if n < 0 else n) for n in nums)
    return unicode_str[::-1]