"""
QUESTION:
Implement a function `roman_to_int(s)` that takes a string `s` representing a Roman numeral and converts it into an integer. The Roman numeral system uses seven symbols (I, V, X, L, C, D, M) representing values 1, 5, 10, 50, 100, 500, and 1000. The conversion rules are as follows: if a smaller value precedes a larger value, it is subtracted from the larger value; if a smaller value follows a larger value, it is added to the larger value.
"""

def roman_to_int(s: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = roman_map[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        if roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    return total