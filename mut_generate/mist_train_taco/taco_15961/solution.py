"""
QUESTION:
How Many Divisors?

Write a program which reads three integers a, b and c, and prints the number of divisors of c between a and b.

Constraints

* 1 ≤ a, b, c ≤ 10000
* a ≤ b

Input

Three integers a, b and c are given in a line separated by a single space.

Output

Print the number of divisors in a line.

Example

Input

5 14 80


Output

3
"""

def count_divisors_in_range(a: int, b: int, c: int) -> int:
    """
    Counts the number of divisors of `c` that lie between `a` and `b` (inclusive).

    Parameters:
    - a (int): The lower bound of the range (inclusive).
    - b (int): The upper bound of the range (inclusive).
    - c (int): The number whose divisors we are counting.

    Returns:
    - int: The number of divisors of `c` in the range [a, b].
    """
    count = 0
    for i in range(a, b + 1):
        if c % i == 0:
            count += 1
    return count