"""
QUESTION:
Problem Description

Apparently, the key that would take Alice home from her Wonderland adventure is a magic pass code hidden in numbers.

Help her find it! It's the one with the highest sum of its digits!

Input Format

Input consists of several integer n, each separated by a newline character.

Output Format

Output Alice's magic code -- the integer with the maximum sum of its digits!

Constraints

0 < n ≤ 100000

SAMPLE INPUT
23
496

SAMPLE OUTPUT
496
"""

def find_magic_code(numbers: list) -> str:
    if not numbers:
        return ""
    
    winner = ''
    max_sum = 0
    
    for num in numbers:
        digit_sum = sum(int(digit) for digit in num)
        if digit_sum > max_sum:
            max_sum = digit_sum
            winner = num
    
    return winner