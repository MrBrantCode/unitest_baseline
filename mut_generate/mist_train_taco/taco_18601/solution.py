"""
QUESTION:
Please find the greatest common divisor of two natural numbers. A clue is: The Euclid's algorithm is a way to resolve this task.



Input

The input file consists of several lines with pairs of two natural numbers in each line. The numbers do not exceed 100000.

The number of pairs (datasets) is less than 50.

Output

Your program has to print the greatest common divisor for each pair of input numbers. Print each result on a new line.

Example

Input

57 38
60 84


Output

19
12
"""

def find_gcd(a: int, b: int) -> int:
    """
    Finds the greatest common divisor (GCD) of two natural numbers using the Euclid's algorithm.

    Parameters:
    a (int): The first natural number.
    b (int): The second natural number.

    Returns:
    int: The greatest common divisor of the two numbers.
    """
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)