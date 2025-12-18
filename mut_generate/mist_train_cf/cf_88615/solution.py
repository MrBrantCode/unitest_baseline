"""
QUESTION:
Write a function `change_case` that takes a string as input and returns the string with the case of each character changed, without using any built-in string case changing functions or methods, or conditional statements for changing the case. The function should have a time complexity of O(n), where n is the length of the string, and should not create any additional arrays or data structures during execution.
"""

def change_case(string):
    result = ""
    for char in string:
        ascii_value = ord(char)
        # check if the character is uppercase
        if ascii_value >= 65 and ascii_value <= 90:
            # convert uppercase to lowercase by adding 32 to ASCII value
            ascii_value += 32
        # check if the character is lowercase
        elif ascii_value >= 97 and ascii_value <= 122:
            # convert lowercase to uppercase by subtracting 32 from ASCII value
            ascii_value -= 32
        result += chr(ascii_value)
    return result