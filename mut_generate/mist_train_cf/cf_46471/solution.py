"""
QUESTION:
Create a function named `check_chars` that takes five parameters: two strings (`string1` and `string2`), two characters (`char1` and `char2`), and an integer (`num`). The function should return `True` if `char1` appears in `string1` exactly `num` times and `char2` appears in `string2` exactly `num` times. Otherwise, it should return `False`.
"""

def check_chars(string1, string2, char1, char2, num):
    return string1.count(char1) == num and string2.count(char2) == num