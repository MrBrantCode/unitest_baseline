"""
QUESTION:
Sorry folks,, admin has no time to create a story for this problem...

You have two integers n and m and you have to print value of factorial(n)%m.

OUTPUT
a single integer containing answer of problem.

Input
23 14567

NOTE You do not need to create a program for this problem you have to write your answers of given input in given code snippet
To see how to submit solution please check this link

SAMPLE INPUT
5 11

SAMPLE OUTPUT
10
"""

def compute_factorial_modulo(n: int, m: int) -> int:
    """
    Computes the factorial of n modulo m.

    Parameters:
    n (int): The number for which the factorial is computed.
    m (int): The modulo value.

    Returns:
    int: The result of factorial(n) % m.
    """
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
    
    fact_n = factorial(n)
    return fact_n % m