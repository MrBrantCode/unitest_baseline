"""
QUESTION:
Write a function `reverse_string(string)` that takes a string as input and returns the reversed string. The function should not use any additional data structures, loops, or recursion, and it should not use any built-in string manipulation functions or methods. The function should have a time complexity of O(n), where n is the length of the string.
"""

def entance(string):
    string_arr = list(string)
    start = 0
    end = len(string_arr) - 1
    while start < end:
        string_arr[start] = chr(ord(string_arr[start]) ^ ord(string_arr[end]))
        string_arr[end] = chr(ord(string_arr[start]) ^ ord(string_arr[end]))
        string_arr[start] = chr(ord(string_arr[start]) ^ ord(string_arr[end]))
        start += 1
        end -= 1
    return ''.join(string_arr)