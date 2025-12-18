"""
QUESTION:
Create a function named `reverse_string` that takes a string as input and returns a new string with all non-whitespace characters reversed. The function should have a time complexity of O(n), where n is the length of the input string, and should be able to handle strings with special characters, punctuation marks, and multiple consecutive whitespace characters. The function should not modify the original string.
"""

def reverse_string(s):
    s = s.replace(" ", "")
    s_list = list(s)
    start = 0
    end = len(s_list) - 1
    while start < end:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
    return ''.join(s_list)