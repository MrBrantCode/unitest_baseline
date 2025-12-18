"""
QUESTION:
Write a function `fizz_buzz_arith_seq(n)` that takes an integer `n` as input and returns the frequency of the digit 7 in integers under `n` that are divisible by either 11 or 13 and form an increasing arithmetic sequence. Assume the common difference of the arithmetic sequence is the divisor (either 11 or 13).
"""

def fizz_buzz_arith_seq(n: int):
    def count_sevens(num: int):
        return str(num).count("7")

    total_sevens = 0
    first = 451 // 11 * 11
    last = (n - 1) // 11 * 11
    for i in range(first, last + 1, 11):
        total_sevens += count_sevens(i)

    first = 442 // 13 * 13
    last = (n - 1) // 13 * 13
    for i in range(first, last + 1, 13):
        total_sevens += count_sevens(i)

    return total_sevens