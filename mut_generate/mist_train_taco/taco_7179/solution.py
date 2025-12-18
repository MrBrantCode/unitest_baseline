"""
QUESTION:
Counting was a difficult task in ancient Rome. The Arabic numerals 0,1,2,3,…, 9 have not yet been disseminated. Instead, the following symbols were used:

Arabic numerals | Roman numerals | Arabic numerals | Roman numerals | Arabic numerals | Roman numerals
--- | --- | --- | --- | --- | ---
1 | I | 11 | XI | 30 | XXX | | 2 | II | 12 | XII | 40 | XL | | 3 | III | 13 | XIII | 50 | L | | 4 | IV | 14 | XIV | 60 | LX | | 5 | V | 15 | XV | 70 | LXX | | 6 | VI | 16 | XVI | 80 | LXXX | | 7 | VII | 17 | XVII | 90 | XC | | 8 | VIII | 18 | XVIII | 100 C | | 9 | IX | 19 | XIX | 500 | D | | 10 | X | 20 | XX | 1000 | M |


I is 1, V is 5, X is 10, L is 50, C is 100, D is 500, M is 1000, see the table above for other examples. Add when a small number follows a large number, that is, on the right side. When the small number is before the large number, that is, to the left, subtract the small number from the large number. There is only one small number in front of the large number that represents the subtraction per subtraction.

Create a program that converts Roman numerals into Arabic numerals (normal numbers) notation (decimal notation) and outputs them. However, the Roman numerals given only follow the above rules (there are more detailed rules for notation of actual Roman numerals, but they do not need to be considered here. For example, is I a V in actual Roman numerals? From X, X only subtracts from L or C, C only subtracts from D or M, and the same Roman numeral does not add more than 4 (or 5).)



Input

Given multiple datasets. Roman numerals (consecutive strings represented by I, V, X, L, C, D, M in half-width uppercase letters) are given to each data set on one line. The length of each Roman numeral string given is 100 or less.

The number of datasets does not exceed 50.

Output

Output Arabic numerals (integers) on one line for each dataset.

Example

Input

IV
CCCCLXXXXVIIII
CDXCIX


Output

4
499
499
"""

def roman_to_arabic(roman_numeral: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_numeral = 0
    values = [roman_values[char] for char in roman_numeral]
    
    for i in range(len(values)):
        if i + 1 < len(values) and values[i] < values[i + 1]:
            arabic_numeral -= values[i]
        else:
            arabic_numeral += values[i]
    
    return arabic_numeral