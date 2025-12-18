"""
QUESTION:
Write a function called `divide_string` that takes a string `s` as input and divides it into three distinct parts. The function should return a formatted string listing the three parts. If the string is not long enough to be divided into three parts (i.e., its length is less than 3), the function should return an error message. If the string's length is not a multiple of 3, the function should also return an error message.
"""

def divide_string(s):
    length = len(s)

    # Error checking
    if length < 3:
        return "Error: The string is too short to be divided into 3 parts."
    elif length % 3 != 0:
        return "Error: The string length is not a multiple of 3."

    part1 = s[0:length//3]
    part2 = s[length//3:2*length//3]
    part3 = s[2*length//3:]

    return f"Part1: {part1}\nPart2: {part2}\nPart3: {part3}"