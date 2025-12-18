"""
QUESTION:
Write a function `calculate_sum` that takes an array of strings or integers as input, calculates the combined sum of the integers and the Roman numeral equivalents, and returns the result. The function should ignore invalid input data and differentiate between Roman numeral-based strings and regular strings. A valid Roman numeral string can consist of the Roman numerals I, V, X, L, C, D, and M. If a string contains a mix of Arabic and Roman numerals, only the Arabic numerals should be considered.
"""

def calculate_sum(arr):
    def roman_to_int(s):
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i - 1]]:
                total += roman_to_int[s[i]] - 2 * roman_to_int[s[i - 1]]
            else:
                total += roman_to_int[s[i]]
        return total

    total = 0
    for i in arr:
        try:
            total += int(i)
        except ValueError:
            if set(i) <= {'I', 'V', 'X', 'L', 'C', 'D', 'M'}:  #checks if i is made up of only valid roman numerals
                total += roman_to_int(i)
    return total