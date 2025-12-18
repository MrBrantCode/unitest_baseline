"""
QUESTION:
Olesya loves numbers consisting of n digits, and Rodion only likes numbers that are divisible by t. Find some number that satisfies both of them.

Your task is: given the n and t print an integer strictly larger than zero consisting of n digits that is divisible by t. If such number doesn't exist, print  - 1.

Input

The single line contains two numbers, n and t (1 ≤ n ≤ 100, 2 ≤ t ≤ 10) — the length of the number and the number it should be divisible by.

Output

Print one such positive number without leading zeroes, — the answer to the problem, or  - 1, if such number doesn't exist. If there are multiple possible answers, you are allowed to print any of them.

Examples

Input

3 2


Output

712
"""

def find_divisible_number(n: int, t: int) -> int:
    # Calculate the range of numbers with n digits
    a = 10 ** (n - 1)
    b = 10 ** n
    
    # Iterate through the range to find a number divisible by t
    for i in range(a, b):
        if i % t == 0:
            return i
    
    # If no such number is found, return -1
    return -1