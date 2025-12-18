"""
QUESTION:
Design a function `mini_roman_to_int(roman)` that converts the input string, stating a number in roman numerals in lowercase, back to its integer form. The roman numeral string input is strictly confined within the range of 'i' to 'm'.
"""

def roman_to_int(s):
    rom_val = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val