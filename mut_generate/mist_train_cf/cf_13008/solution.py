"""
QUESTION:
Create a function `roman_to_integer` that takes a Roman numeral string as input and returns its corresponding integer value. The function should handle cases where a smaller numeral appears before a larger one (e.g., IV for 4). The input string will only contain the characters I, V, X, L, C, D, and M.
"""

def roman_to_integer(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for c in roman_numeral[::-1]:
        current_value = roman_dict[c]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value
    return result