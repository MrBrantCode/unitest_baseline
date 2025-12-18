"""
QUESTION:
Given the function F(n), which represents the count of integers x ≤ n that can be expressed as x = a^2 * b^3, where a and b are integers, not necessarily identical, and both exceed 1, find the value of F(9 * 10^18). The function F(n) should be computed in constant time given the values of n^(1/3), n^(2/3), n, sqrt(n), and cbrt(sqrt(n)).
"""

def entrance(n):
    """
    Calculate the count of integers x ≤ n that can be expressed as x = a^2 * b^3.

    Args:
    n (int): The input number.

    Returns:
    int: The count of integers x ≤ n that can be expressed as x = a^2 * b^3.
    """
    n_1_3 = n ** (1 / 3)
    n_2_3 = n ** (2 / 3)
    n_sqrt = n ** 0.5
    return (
        n_2_3 / 2
        + n_1_3 * n_sqrt / 2
        - n_sqrt * n_1_3 / 2
        + n_1_3 ** 3 / 12
        - n_1_3 ** 3 / 4
        + n_1_3 ** 3 / 12
        - (n ** 0.25) ** 1.5
        - n_1_3 / 4
        + n_1_3 / 2
        - n ** 1.3333333333333333 / 4
    )