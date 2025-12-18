"""
QUESTION:
Write a function `check_conditions` that calculates the sum of all 0 to 9 pandigital numbers that exhibit a distinctive sub-string divisibility property. The pandigital number should have the following properties:
- The 2nd to 4th digits are divisible by 2
- The 3rd to 5th digits are divisible by 3
- The 4th to 6th digits are divisible by 5
- The 5th to 7th digits are divisible by 7
- The 6th to 8th digits are divisible by 11
- The 7th to 9th digits are divisible by 13
- The 8th to 10th digits are divisible by 17
"""

def check_conditions(s):
    divs = [2, 3, 5, 7, 11, 13, 17]
    return all(int(s[i+1:i+4]) % divs[i] == 0 for i in range(len(divs)))