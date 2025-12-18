"""
QUESTION:
Implement a function `roman_numeral_to_int(roman_numeral)` that takes a string of Roman numerals as input and returns its corresponding integer value. The function should handle cases where a smaller numeral appears before a larger one (e.g., IV for 4). The Roman numerals and their corresponding integer values are: I (1), V (5), X (10), L (50), C (100), D (500), and M (1000).
"""

def roman_numeral_to_int(roman_numeral):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    total = 0
    i = 0

    while (i < len(roman_numeral)):
        s1 = values[roman_numeral[i]]

        if (i + 1 < len(roman_numeral)):
            s2 = values[roman_numeral[i + 1]]

            if s1 >= s2:
                total = total + s1
                i = i + 1
            else:
                total = total + s2 - s1
                i = i + 2
        else:
            total = total + s1
            i = i + 1

    return total