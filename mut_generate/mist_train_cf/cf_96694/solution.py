"""
QUESTION:
Write a function `print_reverse(string)` that prints each character of the input string in reverse order, without using any built-in string manipulation functions or loops. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def print_reverse(string):
    if len(string) == 0:
        return
    
    print_reverse(string[1:])  # recursive call with substring starting from the second character
    print(string[0])  # print the first character of the substring