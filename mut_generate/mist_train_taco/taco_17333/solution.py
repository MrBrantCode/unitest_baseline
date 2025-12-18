"""
QUESTION:
find the sum of the even fibonacci numbers till the given number(it is the value not index).
 INPUT:
T test cases
next T lines consists of a number n.
OUTPUT:
Output the sum value.

0<t<10
2<n<10^20
Example:
if n=10
the numbers which are less than 10 are 2 and 8 in fibonacci.
sum = 2+8=10

SAMPLE INPUT
2
10
100

SAMPLE OUTPUT
10
44
"""

def sum_even_fibonacci_numbers(n):
    """
    Calculate the sum of all even Fibonacci numbers less than the given number n.

    Parameters:
    n (int): The upper limit for the Fibonacci numbers to consider.

    Returns:
    int: The sum of all even Fibonacci numbers less than n.
    """
    if n <= 2:
        return 0
    
    sum_even = 0
    a, b = 1, 1
    
    while True:
        a, b = b, a + b
        if b >= n:
            break
        if b % 2 == 0:
            sum_even += b
    
    return sum_even