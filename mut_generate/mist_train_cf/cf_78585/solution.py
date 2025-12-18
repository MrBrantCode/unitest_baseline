"""
QUESTION:
Write a function `fizz_buzz_arith_seq` that takes an integer `n` as input and returns the total count of the digit 7 in all integers less than `n` that are divisible by either 11 or 13. The integers should form an ascending arithmetic sequence.
"""

def fizz_buzz_arith_seq(n: int) -> int:
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count