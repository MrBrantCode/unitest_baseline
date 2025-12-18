"""
QUESTION:
The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. If you repeat the process continuously for n, n will eventually reach 1.

For example, if n = 20, the resulting sequence will be:

[20, 10, 5, 16, 8, 4, 2, 1] 

Write a program that will output the length of the Collatz Conjecture for any given n. In the example above, the output would be 8.

For more reading see: http://en.wikipedia.org/wiki/Collatz_conjecture
"""

def collatz_sequence_length(n):
    """
    Calculate the length of the Collatz sequence for a given natural number n.

    Parameters:
    n (int): The starting natural number for the Collatz sequence.

    Returns:
    int: The length of the Collatz sequence starting from n until it reaches 1.
    """
    step = 1
    while n != 1:
        n = [n // 2, n * 3 + 1][n % 2]
        step += 1
    return step