"""
QUESTION:
Write a function called `reverse_string` that takes a string `str` as input and returns the reversed string. The function should reverse the string without using any built-in string reversal functions. The input string can contain any characters.
"""

def reverse_string(str):
    string = list(str)
    
    start_index = 0
    end_index = len(string) - 1
    
    while start_index < end_index:
        string[start_index], string[end_index] = string[end_index], string[start_index]
        
        start_index += 1
        end_index -= 1
        
    return ''.join(string)