"""
QUESTION:
Implement a function `change_case` that takes a string as input and returns a new string with all alphabetic characters' case changed, leaving punctuation and other non-alphabetic characters unchanged. The function should use a recursive approach with a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def change_case(string):
    if not string:
        return ""

    first_char = string[0]

    if first_char.isalpha():
        return first_char.swapcase() + change_case(string[1:])
    else:
        return first_char + change_case(string[1:])