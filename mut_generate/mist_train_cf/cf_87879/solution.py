"""
QUESTION:
Implement a function `reverse_string` that takes a string `s` as input and returns the reverse of the string. The function should have a time complexity of O(n), where n is the length of the string, and should use constant space. Do not use any built-in string reversal functions or external libraries. The input string will not exceed 10^6 characters.
"""

def reverse_string(s: str) -> str:
    char_list = list(s)
    length = len(s)
    
    for i in range(length // 2):
        temp = char_list[i]
        char_list[i] = char_list[length - i - 1]
        char_list[length - i - 1] = temp
    
    return ''.join(char_list)