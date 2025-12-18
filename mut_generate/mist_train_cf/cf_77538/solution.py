"""
QUESTION:
Create a function `roman_to_decimal(roman)` that converts a given Roman numeral string into its decimal equivalent. The function should take a string `roman` as input and return the corresponding decimal number. The function should handle cases where a smaller numeral appears before a larger one in the Roman numeral string.
"""

def roman_to_decimal(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman):
        if values[char] >= prev_value:
            total += values[char]
        else:
            total -= values[char]
        prev_value = values[char]
    return total