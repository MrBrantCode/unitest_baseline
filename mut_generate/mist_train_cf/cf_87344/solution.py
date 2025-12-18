"""
QUESTION:
Write a function `convert_string_to_int(s: str, multiplier: int) -> int` that takes a string `s` and an integer `multiplier` as input. The function should return the sum of the ASCII values of all characters in `s`, multiplied by `multiplier`. If the sum of the ASCII values is divisible by 3, the function should subtract the ASCII value of the first character from the final result before multiplying by `multiplier`. The input string `s` will consist of 1 to 10^5 alphabetic and/or punctuation characters, and the `multiplier` will be between 1 and 1000.
"""

def entrance(s: str, multiplier: int) -> int:
    ascii_sum = 0

    for ch in s:
        ascii_sum += ord(ch)

    if ascii_sum % 3 == 0 and s:
        ascii_sum -= ord(s[0])

    return ascii_sum * multiplier