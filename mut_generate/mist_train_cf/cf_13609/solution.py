"""
QUESTION:
Write a function `check_string(string)` that takes a string as input and returns a message. The message should include the length of the string. The function should also check if the string contains any numbers and return an error message if it does. Additionally, the function should check if the string is in uppercase and include this information in the message. The input string can be empty.
"""

def check_string(string):
    message = "The length of the string is: "
    length = len(string)
    if length > 0:
        for char in string:
            if char.isdigit():
                return "The string should not contain any numbers."
        message += str(length)
        if string.isupper():
            return message + ", and the string is in uppercase."
        else:
            return message + ", but the string is not in uppercase."
    else:
        return "The string is empty."