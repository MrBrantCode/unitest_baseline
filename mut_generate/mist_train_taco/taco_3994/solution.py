"""
QUESTION:
Jack is a great mathematician. He loves to solve series. Now Stuart gave a
series to Jack and said you have to solve the problem by making a computer program. But Jack doesn't know, how to code.

The series is:

1 + (a1).(x)^1 + (a2).(x)^2 + (a3).(x)^3 +........+(an).(x)^n

And the problem is find the sum of the

a1 + a2 + a3 +.....+ an

Help Jack to find the solution of the problem given by Stuart.

HINT: Here x is the variable and the a1, a2,...  are the constants. Try to find the general solution of the problem.

INPUT:

First line contains the number of test cases T, followed by T lines, each line contains the integer value of n.

OUTPUT:

Display T lines denoting the desired result for each test case.

Constraints:

1 ≤ T ≤ 10

1 ≤ n ≤ 50

SAMPLE INPUT
1
1

SAMPLE OUTPUT
1
"""

def calculate_series_sum(n: int) -> int:
    """
    Calculate the sum of the series a1 + a2 + a3 + ... + an for a given n.

    The series is defined as:
    1 + (a1).(x)^1 + (a2).(x)^2 + (a3).(x)^3 + ... + (an).(x)^n

    The sum of the constants a1 + a2 + a3 + ... + an is calculated as 2^n - 1.

    Parameters:
    n (int): The value of n for which the sum of the series needs to be calculated.

    Returns:
    int: The sum of the series for the given n.
    """
    return 2**n - 1