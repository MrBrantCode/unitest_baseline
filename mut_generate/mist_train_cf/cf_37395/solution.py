"""
QUESTION:
Create a function `roman_to_int(s)` that takes a string `s` representing a Roman numeral and returns its corresponding integer value. The function should handle standard Roman numerals (I, V, X, L, C, D, M) as well as exceptions where a smaller numeral appears before a larger one to indicate subtraction (IV, IX, XL, XC, CD, CM). Assume the input is a valid Roman numeral.
"""

def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    result = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i:i+2] in roman_values:
            result += roman_values[s[i:i+2]]
            i += 2
        else:
            result += roman_values[s[i]]
            i += 1
    return result