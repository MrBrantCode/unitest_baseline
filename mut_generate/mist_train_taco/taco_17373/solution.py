"""
QUESTION:
*Recreation of [Project Euler problem #6](https://projecteuler.net/problem=6)*

Find the difference between the sum of the squares of the first `n` natural numbers `(1 <= n <= 100)` and the square of their sum.

## Example
For example, when `n = 10`:

* The square of the sum of the numbers is:

  (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)^(2) = 55^(2) = 3025


* The sum of the squares of the numbers is:

 1^(2) + 2^(2) + 3^(2) + 4^(2) + 5^(2) + 6^(2) + 7^(2) + 8^(2) + 9^(2) + 10^(2) = 385

Hence the difference between square of the sum of the first ten natural numbers and the sum of the squares of those numbes is: 3025 - 385 = 2640
"""

def calculate_difference_of_squares(n: int) -> int:
    """
    Calculate the difference between the square of the sum and the sum of the squares
    of the first `n` natural numbers.

    Parameters:
    n (int): The number of natural numbers to consider, where 1 <= n <= 100.

    Returns:
    int: The difference between the square of the sum and the sum of the squares.
    """
    r = range(1, n + 1)
    sum_of_squares = sum(z ** 2 for z in r)
    square_of_sum = sum(r) ** 2
    return square_of_sum - sum_of_squares