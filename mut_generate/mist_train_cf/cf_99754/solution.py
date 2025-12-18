"""
QUESTION:
Implement the find_equal_value_pair() function, which takes a list of alphanumeric strings as input and returns a tuple containing the first pair of strings whose sum of ASCII values are equal. If no such pair exists, return None. The function should be optimized for efficiency.
"""

def find_equal_value_pair(strings):
    ascii_sum = {}
    for string in strings:
        sum = 0
        for char in string:
            sum += ord(char)
        if sum in ascii_sum:
            return (ascii_sum[sum], string)
        ascii_sum[sum] = string
    return None