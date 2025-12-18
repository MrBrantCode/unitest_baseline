"""
QUESTION:
Given a number find the number of trailing zeroes in its factorial.

Input Format

A single integer - N

Output Format

Print a single integer which is the number of trailing zeroes.

Input Constraints

1 ≤ N ≤ 1000

Problem Setter: Practo Tech Team

SAMPLE INPUT
10

SAMPLE OUTPUT
2

Explanation

10! = 3628800 has 2 zeros in the end.
"""

def count_trailing_zeros_in_factorial(n: int) -> int:
    if n < 5:
        return 0
    
    power = 0
    divisors = []
    
    while True:
        divisor = 5 ** (power + 1)
        if n < divisor:
            break
        power += 1
        divisors.append(divisor)
    
    return sum(n // divisor for divisor in divisors)