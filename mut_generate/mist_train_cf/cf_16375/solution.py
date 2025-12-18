"""
QUESTION:
Write a function `concatenate_first_last` that takes a string of alphabetic characters with a length between 3 and 100 characters as input. The function should concatenate the first and last characters of the string together, but if the length of the string is odd, it should first remove the middle character. The solution should have a time complexity of O(n), where n is the length of the string.
"""

def concatenate_first_last(s):
    length = len(s)
    if length % 2 == 1:
        middle_index = length // 2
        s = s[:middle_index] + s[middle_index + 1:]
    result = s[0] + s[-1]
    return result