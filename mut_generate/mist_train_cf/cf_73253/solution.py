"""
QUESTION:
Write a function `fizz_buzz_arith_seq(n: int)` that calculates the relative abundance of the digit 7 found within numbers less than the specified integer `n`, which are divisible either by 11 or 13. The function should return the count of the digit 7's found in these numbers.
"""

def fizz_buzz_arith_seq(n: int) -> int:
    count = 0
    for i in range(11, n, 11):
        count += str(i).count('7')
    for i in range(13, n, 13):
        count += str(i).count('7')

    return count