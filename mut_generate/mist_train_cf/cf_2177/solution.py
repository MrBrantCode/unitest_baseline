"""
QUESTION:
Write a function `print_string(string, number)` that prints a given string in reverse order the specified number of times. The string will only contain uppercase and lowercase letters. The function should use a recursive approach and have a time complexity of O(n), where n is the length of the string.
"""

def entrance(s, n):
    if n == 0:
        return
    else:
        print(s[::-1])
        entrance(s, n-1)