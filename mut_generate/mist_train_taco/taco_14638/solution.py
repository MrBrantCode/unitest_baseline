"""
QUESTION:
Write a program which computes the greatest common divisor (GCD) and the least common multiple (LCM) of given a and b.

Constraints

* 0 < a, b ≤ 2,000,000,000
* LCM(a, b) ≤ 2,000,000,000
* The number of data sets ≤ 50

Input

Input consists of several data sets. Each data set contains a and b separated by a single space in a line. The input terminates with EOF.

Output

For each data set, print GCD and LCM separated by a single space in a line.

Example

Input

8 6
50000000 30000000


Output

2 24
10000000 150000000
"""

def compute_gcd_lcm(a: int, b: int) -> tuple:
    """
    Computes the greatest common divisor (GCD) and the least common multiple (LCM) of two integers a and b.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    tuple: A tuple containing the GCD and LCM of a and b.
    """
    def gcd(a, b):
        (a, b) = (max(a, b), min(a, b))
        while b != 0:
            (a, b) = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    gcd_value = gcd(a, b)
    lcm_value = lcm(a, b)
    return (gcd_value, lcm_value)