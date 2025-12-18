"""
QUESTION:
You need to find if a number can be expressed as sum of two perfect powers. That is, given x find if there exists non negative integers a, b, m, n such that am + bn = x.

Input

First line of the input contains number of test cases T. It is followed by T lines, each line contains a sinle number x.

Output

For each test case, print "Yes" (without quotes) if the number can be expressed as sum of two perfect powers. Otherwise print "No" (without quotes).

Constraints

1 ≤ T ≤ 1000

1 ≤ x ≤ 1000000

m > 1, n > 1

SAMPLE INPUT
5
5
15
9
77
100

SAMPLE OUTPUT
Yes
No
Yes
No
Yes
"""

def can_be_sum_of_two_powers(x, max_num=1000000, max_power=1000):
    """
    Checks if a number can be expressed as the sum of two perfect powers.

    Args:
    x (int): The number to check.
    max_num (int, optional): The maximum possible value of the numbers to generate perfect powers. Defaults to 1000000.
    max_power (int, optional): The maximum possible power for generating perfect powers. Defaults to 1000.

    Returns:
    bool: True if the number can be expressed as the sum of two perfect powers, False otherwise.
    """

    # Initialize an array to store the perfect powers
    P = [0] * (max_num + 1)

    # Generate all perfect powers up to max_num
    for i in range(2, max_power + 1):
        j = 2
        while int(pow(i, j)) <= max_num:
            pos = int(pow(i, j))
            P[pos] = 1
            j += 1

    # 1 is a perfect power (1^2)
    P[1] = 1

    # Check if x can be expressed as the sum of two perfect powers
    for i in range(1, (x >> 1) + 1):
        if P[i] and P[x - i]:
            return True

    return False