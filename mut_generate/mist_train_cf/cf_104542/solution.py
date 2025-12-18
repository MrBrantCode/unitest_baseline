"""
QUESTION:
Generate a function `generate_odd_numbers(n)` that returns a list containing only the odd numbers from 1 to `n`, excluding multiples of 3. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def generate_odd_numbers(n):
    """
    Returns a list of odd numbers from 1 to n, excluding multiples of 3.

    Time complexity: O(n)
    Space complexity: O(n)

    :param n: The upper limit for generating odd numbers.
    :return: A list of odd numbers excluding multiples of 3.
    """
    return [i for i in range(1, n+1) if i % 2 != 0 and i % 3 != 0]