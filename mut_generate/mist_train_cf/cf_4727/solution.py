"""
QUESTION:
Implement a function `change_case` that takes a string as input and returns a new string with the case of each character changed, without using built-in string case changing functions or methods. The function should not use any conditional statements for changing the case of each character and should not create any additional arrays or data structures during execution. The time complexity should be O(n), where n is the length of the string.
"""

def change_case(string):
    result = ""
    for char in string:
        ascii_value = ord(char)
        result += chr(ascii_value + (32 if ascii_value >= 65 and ascii_value <= 90 else -32 if ascii_value >= 97 and ascii_value <= 122 else 0))
    return result