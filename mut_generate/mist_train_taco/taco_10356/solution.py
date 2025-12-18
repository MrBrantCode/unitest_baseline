"""
QUESTION:
Little Petya loves inequations. Help him find n positive integers a1, a2, ..., an, such that the following two conditions are satisfied:

  * a12 + a22 + ... + an2 ≥ x
  * a1 + a2 + ... + an ≤ y

Input

The first line contains three space-separated integers n, x and y (1 ≤ n ≤ 105, 1 ≤ x ≤ 1012, 1 ≤ y ≤ 106).

Please do not use the %lld specificator to read or write 64-bit integers in С++. It is recommended to use cin, cout streams or the %I64d specificator.

Output

Print n positive integers that satisfy the conditions, one integer per line. If such numbers do not exist, print a single number "-1". If there are several solutions, print any of them.

Examples

Input

5 15 15


Output

4
4
1
1
2


Input

2 3 2


Output

-1


Input

1 99 11


Output

11
"""

def find_positive_integers(n, x, y):
    """
    Finds n positive integers a1, a2, ..., an such that:
    1. a1^2 + a2^2 + ... + an^2 ≥ x
    2. a1 + a2 + ... + an ≤ y

    Parameters:
    n (int): The number of positive integers to find.
    x (int): The minimum sum of squares of the integers.
    y (int): The maximum sum of the integers.

    Returns:
    list: A list of n positive integers that satisfy the conditions, or -1 if no such integers exist.
    """
    from math import sqrt, ceil
    
    if x < n:
        t = 1
    else:
        t = ceil(sqrt(x - n + 1))
    
    if t + n - 1 > y:
        return -1
    else:
        return [t] + [1] * (n - 1)