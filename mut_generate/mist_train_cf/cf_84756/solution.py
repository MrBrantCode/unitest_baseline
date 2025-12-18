"""
QUESTION:
Create a function called `start_end_palindrome` that checks if the input string starts and ends with a palindrome sequence of characters. The function should return `True` if the string meets the condition and `False` otherwise. The function should not be restricted to a specific length or type of input string.
"""

def is_palindrome(s):
    return s == s[::-1]

def start_end_palindrome(input_string):
    for i in range(len(input_string), -1, -1):
        if is_palindrome(input_string[0:i]):
            for j in range(0, len(input_string[i:])+1):
                if is_palindrome(input_string[i:i+j]):
                    return True
    return False