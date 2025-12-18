"""
QUESTION:
Create a function `convert_string_to_int(s: str, multiplier: int) -> int:` that takes a string `s` and an integer `multiplier` as inputs, calculates the sum of the ASCII values of all characters in the string, multiplies it by the given multiplier, and if the sum is divisible by 3, subtracts the ASCII value of the first character from the result. The string `s` consists of 1 to 10^5 alphabetic and/or punctuation characters, and the multiplier is an integer between 1 and 1000. Return the converted integer value.
"""

def convert_string_to_int(s: str, multiplier: int) -> int:
    ascii_sum = 0
    for char in s:
        ascii_sum += ord(char)
    
    if ascii_sum % 3 == 0 and s:
        ascii_sum -= ord(s[0])
    
    return ascii_sum * multiplier