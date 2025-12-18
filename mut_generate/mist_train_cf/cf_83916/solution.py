"""
QUESTION:
Write a function called `numListToRoman` that takes a list of integers as input and returns a list of strings representing the corresponding Roman numerals. The function should have a time complexity of O(n), where n is the number of integers in the input list.
"""

def numListToRoman(num_list):
    mapping = {
        1:    "I",
        4:    "IV",
        5:    "V",
        9:    "IX",
        10:   "X",
        40:   "XL",
        50:   "L",
        90:   "XC",
        100:  "C",
        400:  "CD",
        500:  "D",
        900:  "CM",
        1000: "M"
    }

    def intToRoman(num):
        roman = ""
        for value in sorted(mapping.keys(), reverse=True):
            while num >= value:
                num -= value
                roman += mapping[value]
        return roman

    return [intToRoman(num) for num in num_list]