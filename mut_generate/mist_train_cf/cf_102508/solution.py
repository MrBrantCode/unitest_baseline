"""
QUESTION:
Write a function `function(message)` that takes a string `message` of maximum length 1000 as input and returns a reversed version of the string. The function should handle cases where the input string contains special characters, numbers, uppercase letters, emojis, and non-ASCII characters, while preserving their order. The function should also ignore leading and trailing whitespace characters in the input string.
"""

def reverse_string(message):
    message = message.strip()
    message_list = list(message)
    message_list.reverse()
    reversed_message = ''.join(message_list)
    return reversed_message