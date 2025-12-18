"""
QUESTION:
Write a function `five_div_prime_seq(n)` to calculate and return the occurrence of the digit 5 in numbers below the value `n` that are divisible by either 9 or 14 and form a decreasing geometric sequence.
"""

def five_div_prime_seq(n):
    count = 0
    for i in range(2, n):
        if i % 9 == 0 or i % 14 == 0:
            count += str(i).count('5')
    return count