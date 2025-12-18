"""
QUESTION:
Write a function named `string_to_float` that takes a string of a valid positive decimal number with up to 2 decimal places and returns its float representation. The function should handle leading and trailing whitespace in the string and must not use any built-in conversion functions or libraries.
"""

def string_to_float(s):
    s = s.strip() 
    decimal_index = -1 
    for i in range(len(s)):
        if s[i] == '.':
            decimal_index = i 
            break

    float_value = 0.0
    for i in range(len(s)):
        if i != decimal_index:
            digit = ord(s[i]) - ord('0') 
            float_value = float_value * 10 + digit

    if decimal_index != -1:
        decimal_places = len(s) - decimal_index - 1
        float_value = float_value / (10 ** decimal_places)
    
    return float_value