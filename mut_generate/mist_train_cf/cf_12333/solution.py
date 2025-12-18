"""
QUESTION:
Implement a function named `reverse_string(s)` that reverses the input string `s` without using any built-in string reversal functions. The function should achieve a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. The input string `s` is expected to be a string of characters, and the output should be the reversed string.
"""

def reverse_string(s):
    string_list = list(s)
    start = 0
    end = len(string_list) - 1
    
    while start < end:
        string_list[start], string_list[end] = string_list[end], string_list[start]
        start += 1
        end -= 1
    
    reversed_string = ''.join(string_list)
    return reversed_string